import sys,os
import time
import ctypes
from ctypes import cdll
from ctypes import CDLL
from ctypes import c_int
from ctypes import c_uint
from ctypes import pointer
from ctypes import c_char_p
from ctypes import c_float
from ctypes import c_double
from ctypes import byref
from threading import Thread
import shutil
import json
import glob

''' Modules for processing
    FE provides functions for feature extraction
    CF provides functions for classification and managing classifier
    AQ provides functions for data acquisition
    PP provides functions for pre processing EEG data
'''
import feature_extraction as FE
import eeg_classification as CF
import preprocessing as PP
from sklearn.feature_selection import RFE
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import numpy as np

import acquisition as AQ
from front_end_client import *

import sensor_fusion as SF

''' Check if libEDK exists'''
try :
    if sys.platform.startswith('win32'):
        libEDK = cdll.LoadLibrary("edk.dll")
    if sys.platform.startswith('linux'):
        srcDir = os.getcwd()
        libPath = srcDir + "/libedk.so.1.0.0"
        libEDK = CDLL(libPath)
except :
    print 'Error : cannot load dll lib'


ED_COUNTER = 0
ED_INTERPOLATED=1
ED_RAW_CQ=2
ED_AF3=3
ED_F7=4
ED_F3=5
ED_FC5=6
ED_T7=7
ED_P7=8
ED_O1=9
ED_O2=10
ED_P8=11
ED_T8=12
ED_FC6=13
ED_F4=14
ED_F8=15
ED_AF4=16
ED_GYROX=17
ED_GYROY=18
ED_TIMESTAMP=19
ED_ES_TIMESTAMP=20
ED_FUNC_ID=21
ED_FUNC_VALUE=22
ED_MARKER=23
ED_SYNC_SIGNAL=24

targetChannelList = [ED_COUNTER,ED_AF3, ED_F7, ED_F3, ED_FC5, ED_T7,ED_P7, ED_O1, ED_O2, ED_P8, ED_T8,ED_FC6, ED_F4, ED_F8, ED_AF4, ED_GYROX, ED_GYROY, ED_TIMESTAMP, ED_FUNC_ID, ED_FUNC_VALUE, ED_MARKER, ED_SYNC_SIGNAL]
header = ['COUNTER','AF3','F7','F3', 'FC5', 'T7', 'P7', 'O1', 'O2','P8', 'T8', 'FC6', 'F4','F8', 'AF4','GYROX', 'GYROY', 'TIMESTAMP','FUNC_ID', 'FUNC_VALUE', 'MARKER', 'SYNC_SIGNAL']
write = sys.stdout.write
eEvent      = libEDK.EE_EmoEngineEventCreate()
eState      = libEDK.EE_EmoStateCreate()
userID            = c_uint(0)
nSamples   = c_uint(0)
nSam       = c_uint(0)
nSamplesTaken  = pointer(nSamples)
#da = zeros(128,double)
data     = pointer(c_double(0))
user                    = pointer(userID)
composerPort          = c_uint(1726)
secs      = c_float(1)
datarate    = c_uint(0)
readytocollect    = False
option      = c_int(0)
state     = c_int(0)


try :
    if sys.platform.startswith('win32'):
        libEDK = cdll.LoadLibrary("edk.dll")
    if sys.platform.startswith('linux'):
        srcDir = os.getcwd()
        libPath = srcDir + "/libedk.so.1.0.0"
        libEDK = CDLL(libPath)
except :
    print 'Error : cannot load dll lib'


print libEDK.EE_EngineConnect("Emotiv Systems-5")
if libEDK.EE_EngineConnect("Emotiv Systems-5") != 0:
    print "Emotiv Engine start up failed."

hData = libEDK.EE_DataCreate()
libEDK.EE_DataSetBufferSizeInSec(secs)


TRARINING_TIME_FOR_A_STATE = 20.0
def acquire_data_for_command(id='tu' ,state_number=0):
    global readytocollect
    file_name = AQ.make_file_name(id, state_number)
    file(file_name, 'w')
    f = open(file_name , 'w')
    print >> f, header
    start = time.time()
    print "Training for state %d will start in 5 second. Please prepare" % state_number
    print "Training will take 20 seconds"
    while time.time() - start < 5.0:
        pass
    start = time.time()
    while time.time() - start < TRARINING_TIME_FOR_A_STATE:
        state = libEDK.EE_EngineGetNextEvent(eEvent)
        print state
        if state == 0:
            eventType = libEDK.EE_EmoEngineEventGetType(eEvent)
            libEDK.EE_EmoEngineEventGetUserId(eEvent, user)
            print eventType
            if eventType == 16 or eventType==64: #libEDK.EE_Event_enum.EE_UserAdded:
                print "User added"
                libEDK.EE_DataAcquisitionEnable(userID,True)
                readytocollect = True

        if readytocollect==True:
            libEDK.EE_DataUpdateHandle(0, hData)
            libEDK.EE_DataGetNumberOfSample(hData,nSamplesTaken)
            print "Updated :",nSamplesTaken[0]
            if nSamplesTaken[0] != 0:
                nSam=nSamplesTaken[0]
                arr=(ctypes.c_double*nSamplesTaken[0])()
                ctypes.cast(arr, ctypes.POINTER(ctypes.c_double))
                for sampleIdx in range(nSamplesTaken[0]):
                    for i in range(22):
                        libEDK.EE_DataGet(hData,targetChannelList[i],byref(arr), nSam)
                        print arr[sampleIdx]
                        print >>f,arr[sampleIdx],",",
                    print >>f,'\n'
        time.sleep(0.2)
    readytocollect = False

COMMAND_TABLES = ["NEUTRAL", "UP", "DOWN", "RIGHT", "LEFT", "FORWARD", "BACKWARD"]


FINAL_COMMAND = SF.SensorFusion()

def acquire_data(id, command_name):
    command_name = command_name.upper()
    if command_name.upper() in COMMAND_TABLES:
        acquire_data_for_command(id, COMMAND_TABLES.index(command_name.upper()))

def reset(id):
    import acquisition as AQ
    AQ.reset_data(id)

def train(id, list_of_commands):
    list_of_commands=[COMMAND_TABLES.index(command.upper()) for command in list_of_commands]
    CF.training(id, list_of_commands)


class RecognitionState:
    def __init__(self):
        self.stop = False
        self.is_reading = False
        self.buffer = [[] for i in range(14)]
        self.header = {'AF3': 0, 'F7': 1, 'F3': 2, 'FC5': 3, 'T7': 4, 'P7': 5,
                      'O1': 6, 'O2': 7, 'P8': 8, 'T8': 9, 'FC6': 10, 'F4': 11,
                      'F8': 12, 'AF4': 13}
        self.time_info = []

    def store_data(self, channel_num, data):
        self.buffer[channel_num].append(data)

    def store_time(self, time):
        self.time_info.append(time);

    def get_buffer_size(self):
        return len(self.buffer[0])

    def reset_buffer(self, half = False):
        if half:
            self.buffer = [channel_data[len(channel_data)/2:] for channel_data in self.buffer]
            self.time_info = self.time_info[len(self.time_info)/2:]
        else:
            self.buffer = [[] for i in range(14)]
            self.time_info = []

recognition_state = RecognitionState()



def stop_recognition():
    global recognition_state
    recognition_state.stop = True
def acquire_data_for_executing():
    global recognition_state
    file("running_data.csv", 'w')
    f = open("running_data.csv" , 'w')
    print >> f, header
    hData = libEDK.EE_DataCreate()
    libEDK.EE_DataSetBufferSizeInSec(secs)
    readytocollect = False
    state = libEDK.EE_EngineGetNextEvent(eEvent)
    while not recognition_state.stop:
        while recognition_state.is_reading:
            pass
        print state
        state = libEDK.EE_EngineGetNextEvent(eEvent)
        if state == 0:
            eventType = libEDK.EE_EmoEngineEventGetType(eEvent)
            print eventType
            libEDK.EE_EmoEngineEventGetUserId(eEvent, user)
            if eventType== 16 or eventType == 64: #libEDK.EE_Event_enum.EE_UserAdded:
                print "User added"
                libEDK.EE_DataAcquisitionEnable(userID,True)
                readytocollect = True

        if readytocollect==True:
            libEDK.EE_DataUpdateHandle(0, hData)
            libEDK.EE_DataGetNumberOfSample(hData,nSamplesTaken)
            print "Updated :",nSamplesTaken[0]
            if nSamplesTaken[0] != 0:
                nSam=nSamplesTaken[0]
                arr=(ctypes.c_double*nSamplesTaken[0])()
                ctypes.cast(arr, ctypes.POINTER(ctypes.c_double))
                for sampleIdx in range(nSamplesTaken[0]):
                    for i in range(22):
                        libEDK.EE_DataGet(hData,targetChannelList[i],byref(arr), nSam)
                        if i >= 1 and i <= 14:
                            recognition_state.store_data(i-1, arr[sampleIdx])
                        if i == 17:
                            recognition_state.store_time(arr[sampleIdx])
                        print >>f,arr[sampleIdx],",",
                    print >>f,'\n'
        time.sleep(0.2)
        recognition_state.is_reading = True

FRONT_END = FrontEndClient()

def send_command_to_front_end(command):
    with open("test1.txt", "a") as myfile:
        myfile.write(str(command))
    COMMAND_MAP = {0: 'neutral', 1: 'move_up', 2: 'move_down', 3: 'move_right', 4: 'move_left', 5: 'move_forward', 6: 'move_backward'}
    if command in COMMAND_MAP.keys():
        FRONT_END.call_method(COMMAND_MAP[command])
        time.sleep(0.5)
        FRONT_END.call_method("neutral")

def executing(clfs, test_features, command_classes,  training_mode = None):
    global recognition_state
    header = {'AF3': 0, 'F7': 1, 'F3': 2, 'FC5': 3, 'T7': 4, 'P7': 5,
              'O1': 6, 'O2': 7, 'P8': 8, 'T8': 9, 'FC6': 10, 'F4': 11,
              'F8': 12, 'AF4': 13}

    accumulator = CommandOnData(clfs, test_features, command_classes)
    while not recognition_state.stop:
        while not recognition_state.is_reading:
            pass
        if recognition_state.get_buffer_size() > 100:
            accumulator.add_data(recognition_state.buffer, recognition_state.time_info)
            if accumulator.is_enough():
                accum_data = accumulator.process()
                command = accumulator.determine_command(accum_data)
                FINAL_COMMAND.drone_command.update_command(command-1)
                print "xxxxxxxxxxxxxxxx"
                print command
                if training_mode:
                    print "input command"
                    correct_command = input()
                    if command != correct_command:
                        accumulator.fix_to(accum_data, correct_command)
                accumulator.reset_buffer()
            recognition_state.reset_buffer(half = False)
        recognition_state.is_reading = False

class CommandOnData:
    def __init__(self, classifiers, test_features, command_classes):
        self.test_features = test_features
        self.command_classes = command_classes
        self.buffer = []
        self.time_info = []
        self.clfs = classifiers

    def add_data(self, buffer, time_info):
        self.buffer.append(buffer)
        self.time_info.append(time_info)

    def is_enough(self):
        return len(self.buffer) >= 2

    def process(self):
        accummulated_result = []
        for data in self.buffer:
            accummulated_result.append(CF.final_command(self.clfs, data))
        print accummulated_result
        return accummulated_result

    def reset_buffer(self):
        self.buffer = []
        self.time_info = []

    def determine_command(self, accumulated_results):
        final_result = {}
        for command, probability in accumulated_results:
            if not final_result.has_key(command):
                final_result[command] = probability
            else:
                final_result[command] += probability
        print final_result
        cmd = -1
        result = 0
        for command in final_result.keys():
            if final_result[command] > result:
                result = final_result[command]
                cmd = command
        print cmd
        return cmd

    def fix_to(self, accum_data, correct_command):
        CHANNELS = ['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7','O1', 'O2', 'P8', 'T8', 'FC6', 'F4','F8', 'AF4', 'COMBINED']
        clf_info = None
        for cf in self.clfs:
            if "-" in cf.channel:
                clf_info = cf
                break
        channels = [CHANNELS.index(name) for name in clf_info.channel.split("-")]
        print channels
        test_f = self.test_features + []
        classes = self.command_classes + []
        for data in self.buffer:
            sub_data = np.array([0.0 for i in data[0]])
            for i in channels:
                sub_data += np.array(data[i])
            test_f.append(FE.compute_feature_vector(sub_data))
            classes.append(correct_command)
        clf_info.clf.fit(test_f, classes)
        # for i in range(len(self.clfs)):
        #     if not ("-" in self.clfs[i].channel):
        #         test_f = self.test_features[i] + []
        #         for data in self.buffer:
        #             sub_data = data[CHANNELS.index(self.clfs[i].channel)]
        #             test_f.append(FE.compute_feature_vector(sub_data))
        #         print test_f
        #         classes = self.command_classes[i] + [correct_command for d in accum_data]
        #         print i
        #         self.clfs[i].clf.fit(test_f, classes)


def recognize(id, list_of_commands=["up", "down"]):
    print "Start running"
    header = {'AF3': 0, 'F7': 1, 'F3': 2, 'FC5': 3, 'T7': 4, 'P7': 5,
              'O1': 6, 'O2': 7, 'P8': 8, 'T8': 9, 'FC6': 10, 'F4': 11,
              'F8': 12, 'AF4': 13}
    CHANNELS = ['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7','O1', 'O2', 'P8', 'T8', 'FC6', 'F4','F8', 'AF4', 'COMBINED']

    global recognition_state
    recognition_state.stop = False
    classifiers = CF.get_classifiers(id)
    clf_info = None
    for cf in classifiers:
        if "-" in cf.channel:
            clf_info = cf
            break
    list_of_commands = [command.upper() for command in list_of_commands]
    channels = [CHANNELS.index(name) for name in clf_info.channel.split("-")]
    test_features = []
    for command in [1,2]:
        user_data = AQ.get_data(id, command)[0]['data']
        data = np.array([0.0 for i in user_data[0]])
        for i in channels:
            data += np.array(user_data[i])
        test_features.append(FE.compute_feature_vector(data))



    # list_of_commands = [COMMAND_TABLES.index(command.upper()) for command in list_of_commands]
    # classifier_columns = [header[clf.channel] for clf in [classifierss for classifierss in classifierss if not ("-" in )]]
    # test_data = []
    # for command in list_of_commands:
    #     user_data = AQ.get_data(id, command)
    #     command_test_data = [[] for i in range(len(classifier_columns))]
    #     for sample in user_data:
    #         t, test_d = AQ.split_data_for_training(sample['data'])
    #         for index, column in zip(range(len(classifier_columns)), classifier_columns):
    #             command_test_data[index] += test_d[column]
    #     test_data.append(command_test_data)
    #
    # features = [[] for i in range(len(classifiers))]
    # classes = [[] for i in range(len(classifiers))]
    # for command, command_data in zip(list_of_commands, test_data):
    #     for index, row in zip(range(len(classifiers)),command_data):
    #         for i in xrange(0, len(row) - 100, 50):
    #             features[index].append(FE.compute_feature_vector(row[i: i+100]))
    #             classes[index].append(command)
    # print classes
    #control variables and buffer
    stop_collecting = False
    acquire_data = Thread(target=acquire_data_for_executing)
    execu = Thread(target=executing, args=(classifiers, test_features, list_of_commands, ))
    acquire_data.start()
    execu.start()
    acquire_data.join()
    execu.join()



def create_user_profile(username):
    ''' API
        Effect: create folders in classifier and userdata folder if not exist
    '''
    username = username.lower()
    if not os.path.isdir('./userdata/' + username):
        os.makedirs('./userdata/' + username)
    if not os.path.isdir('./classifier/' + username):
        os.makedirs('./classifier/' + username)


def delete_user_profile(username):
    ''' API
        Effect: Remove folders with username name in classifier and userdata folers.
    '''
    shutil.rmtree('./userdata/' + username)
    shutil.rmtree('./classifier/' + username)

def delete_user_data(username, command):
    username = username.lower()
    command = command.upper()
    if command in COMMAND_TABLES:
        for name in glob.glob('userdata/' + username + '/' + command + "_" + username + '_' +"[0-9]*.csv"):
            print name
            os.remove(name)

def get_user_profiles():
    ''' API
        return list of users registered to the application, and samples collected
    '''
    profiles = {}
    for sub_folder in os.listdir('./userdata'):
        profiles[sub_folder] = {}
        folder_path = './userdata/' + sub_folder
        for the_file in os.listdir(folder_path):
            command, id, index = the_file.replace(".csv", "").split("_")
            if profiles[sub_folder].has_key(command):
                profiles[sub_folder][command] += 1
            else:
                profiles[sub_folder][command] = 1
    return profiles

def update_sensor_data(sensor_data):
    'expect a list of 4 sensor data, enumerate: 1 2 3 4'
    FINAL_COMMAND.update_sensor_data(sensor_data)



def get_user_profile(username):
    '''API
        effect: create_user_profile with username if the user is not registered
        return user' list of sample collected
    '''
    username = username.lower()
    profile = {}
    folder_path = './userdata/' + username
    if os.path.isdir(folder_path):
        for the_file in os.listdir(folder_path):
            command, id, index = the_file.replace(".csv", "").split("_")
            if profile.has_key(command):
                profile[command] += 1
            else:
                profile[command] = 1
    else:
        create_user_profile(username)
    return profile
