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

import acquisition as AQ
from front_end_client import *

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


COMMAND_TABLES = ["NEUTRAL", "UP", "DOWN", "RIGHT", "LEFT", "FORWARD", "BACKWARD"]


def acquire_data(id, command_name):
    import acquisition as AQ
    AQ = reload(AQ)
    command_name = command_name.upper()
    if command_name.upper() in COMMAND_TABLES:
        AQ.acquire_data_for_command(id, COMMAND_TABLES.index(command_name.upper()))

def reset(id):
    import acquisition as AQ
    AQ.reset_data(id)

def train(id, list_of_commands):
    list_of_commands=[COMMAND_TABLES.index(command.upper()) for command in list_of_commands]
    CF.training(id, list_of_commands)


class EEGStorage:
    def __init__(self):
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

eeg_storage = EEGStorage()

def acquire_data_for_executing():
    global eeg_storage
    hData = libEDK.EE_DataCreate()
    libEDK.EE_DataSetBufferSizeInSec(secs)
    readytocollect = False
    state = libEDK.EE_EngineGetNextEvent(eEvent)
    while 1:
        while eeg_storage.is_reading:
            pass

        state = libEDK.EE_EngineGetNextEvent(eEvent)
        if state == 0:
            eventType = libEDK.EE_EmoEngineEventGetType(eEvent)
            print eventType
            libEDK.EE_EmoEngineEventGetUserId(eEvent, user)
            if eventType == 64: #libEDK.EE_Event_enum.EE_UserAdded:
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
                            eeg_storage.store_data(i-1, arr[sampleIdx])
                        if i == 17:
                            eeg_storage.store_time(arr[sampleIdx])
        time.sleep(0.2)
        eeg_storage.is_reading = True

FRONT_END = FrontEndClient()

def send_command_to_front_end(command):
    COMMAND_MAP = {0: 'neutral', 1: 'move_up', 2: 'move_down', 3: 'turn_right', 4: 'turn_left', 5: 'move_forward', 6: 'move_backward'}
    if command in COMMAND_MAP.keys():
        FRONT_END.call_method(COMMAND_MAP[command])
        time.sleep(0.5)
        FRONT_END.call_method("neutral")

def executing(clfs):
    global eeg_storage
    header = {'AF3': 0, 'F7': 1, 'F3': 2, 'FC5': 3, 'T7': 4, 'P7': 5,
              'O1': 6, 'O2': 7, 'P8': 8, 'T8': 9, 'FC6': 10, 'F4': 11,
              'F8': 12, 'AF4': 13}

    accumulator = AccumulatedData(clfs)
    while 1:
        while not eeg_storage.is_reading:
            pass
        if eeg_storage.get_buffer_size() > 100:
            accumulator.add_data(eeg_storage.buffer, eeg_storage.time_info)
            if accumulator.is_enough():
                command = accumulator.determine_command(accumulator.process())
                send_command_to_front_end(command)
            eeg_storage.reset_buffer(half = True)
        eeg_storage.is_reading = False

class AccumulatedData:
    def __init__(self, classifiers):
        self.buffer = []
        self.time_info = []
        self.clfs = classifiers

    def add_data(self, buffer, time_info):
        self.buffer.append(buffer)
        self.time_info.append(time_info)

    def is_enough(self):
        return len(self.buffer) > 4

    def process(self):
        accummulated_result = []
        for data in self.buffer:
            accummulated_result.append(CF.final_command(self.clfs, data))
        self.buffer = []
        self.time_info = []
        print accummulated_result
        return accummulated_result

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

def recognize(id):
    classifiers = CF.get_classifiers(id)
    #control variables and buffer
    stop_collecting = False
    acquire_data = Thread(target=acquire_data_for_executing)
    execu = Thread(target=executing, args=(classifiers,))
    acquire_data.start()
    execu.start()
    acquire_data.join()
    execu.join()

recognize("tu")
