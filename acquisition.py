# python version >= 2.5
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

import glob

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


print libEDK.EE_EngineConnect("Emotiv Systems-5")
if libEDK.EE_EngineConnect("Emotiv Systems-5") != 0:
    print "Emotiv Engine start up failed."

MAX_NUMBER_OF_STATES = 6
MIN_NUMBER_OF_STATES = 2

STATE1 = 'UP'

STATE2 = 'DOWN'

STATE3 = 'RIGHT'

STATE4 = 'LEFT'

STATE5 = 'FORWARD'

STATE6 = 'BACKWARD'


STATE_FILES = [STATE1, STATE2, STATE3, STATE4, STATE5, STATE6]

TRARINING_TIME_FOR_A_STATE = 20.0
def acquire_for_training():
    hData = libEDK.EE_DataCreate()
    libEDK.EE_DataSetBufferSizeInSec(secs)
    print "Enter number of states (legal number is 2 to 6): "
    while 1:
        number_of_states = int(raw_input())
        print number_of_states
        if number_of_states < MAX_NUMBER_OF_STATES or number_of_states > MIN_NUMBER_OF_STATES:
            break
        else:
            print "Please re-enter the number of states"
    for i, file_name in zip(range(number_of_states), STATE_FILES):
        f = open(file_name, 'w')
        print >> f, header
        start = time.time()
        print "Training for state %d will start in 5 second. Please prepare" %(i+1)
        print "Training will take 20 seconds"
        print "Input any key to start training"
        raw_input()
        while time.time() - start < 5.0:
            pass
        start = time.time()
        while time.time() - start < TRARINING_TIME_FOR_A_STATE:
            state = libEDK.EE_EngineGetNextEvent(eEvent)
            if state == 0:
                eventType = libEDK.EE_EmoEngineEventGetType(eEvent)
                libEDK.EE_EmoEngineEventGetUserId(eEvent, user)
                if eventType == 16: #libEDK.EE_Event_enum.EE_UserAdded:
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
    libEDK.EE_DataFree(hData)
    libEDK.EE_EngineDisconnect()
    libEDK.EE_EmoStateFree(eState)
    libEDK.EE_EmoEngineEventFree(eEvent)


FOLDER_NAME = 'userdata'
def make_file_name(id, state_number):
    global FOLDER_NAME
    file_name = ''
    i = 0
    while 1:
        file_name = FOLDER_NAME + '/' + STATE_FILES[state_number] + '_' + id + '_' + str(i) + '.csv'
        if not os.path.isfile(file_name):
            break
        i += 1
    return file_name
libEDK.EE_DataSetBufferSizeInSec(secs)
def acquire_data_for_command(id='tu' ,state_number=0):
    file_name = make_file_name(id, state_number)
    file(file_name, 'w')
    f = open(file_name , 'w')
    print >> f, header
    hData = libEDK.EE_DataCreate()
    start = time.time()
    print "Training for state %d will start in 5 second. Please prepare" % state_number
    print "Training will take 20 seconds"
    while time.time() - start < 5.0:
        pass
    start = time.time()
    while time.time() - start < TRARINING_TIME_FOR_A_STATE:
        state = libEDK.EE_EngineGetNextEvent(eEvent)
        if state == 0:
            eventType = libEDK.EE_EmoEngineEventGetType(eEvent)
            libEDK.EE_EmoEngineEventGetUserId(eEvent, user)
            if eventType == 16: #libEDK.EE_Event_enum.EE_UserAdded:
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
    libEDK.EE_DataFree(hData)
    libEDK.EE_EngineDisconnect()
    libEDK.EE_EmoStateFree(eState)
    libEDK.EE_EmoEngineEventFree(eEvent)


def acquire_data_for_executing(buffer, time_info):
    hData = libEDK.EE_DataCreate()
    libEDK.EE_DataSetBufferSizeInSec(secs)
    readytocollect = False
    state = libEDK.EE_EngineGetNextEvent(eEvent)
    while not stop_collecting:
        state = libEDK.EE_EngineGetNextEvent(eEvent)
        if state == 0:
            eventType = libEDK.EE_EmoEngineEventGetType(eEvent)
            libEDK.EE_EmoEngineEventGetUserId(eEvent, user)
            if eventType == 16: #libEDK.EE_Event_enum.EE_UserAdded:
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
                    print "ssssssssssssssssssssssssssssssssss"
                    for i in range(22):
                        libEDK.EE_DataGet(hData,targetChannelList[i],byref(arr), nSam)
                        if i >= 1 and i <= 14:
                            buffer[i-1].append(arr[sampleIdx])
                        if i == 17:
                            time_info.append(arr[sampleIdx])


def get_data(id='tu', state_number=0):
    data = [read_file(name) for name in glob.glob(FOLDER_NAME+'/'+STATE_FILES[state_number]+'_' + id +'_[0-9]*.csv')]
    return data

def split_data_for_training(data_list):
    '''split data for training and testing
       input: 2d array of data
       output: tupple of training data (90% of the data) and test_data(10%)
    '''
    data_len = len(data_list[0])
    training_len = int(0.8*data_len)
    return ([channel_data[0:training_len] for channel_data in data_list], [channel_data[training_len:] for channel_data in data_list])


def read_file(name):
    ret = {}
    ret['header'] = {}
    ret['data'] = [[] for i in range(14)]
    ret['header']['AF3'] = 0
    ret['header']['F7'] = 1
    ret['header']['F3'] = 2
    ret['header']['FC5'] = 3
    ret['header']['T7'] = 4
    ret['header']['P7'] = 5
    ret['header']['O1'] = 6
    ret['header']['O2'] = 7
    ret['header']['P8'] = 8
    ret['header']['T8'] = 9
    ret['header']['FC6'] = 10
    ret['header']['F4'] = 11
    ret['header']['F8'] = 12
    ret['header']['AF4'] = 13
    f = open(name, 'r')
    data = f.read().split('\n')
    for i, d in zip(range(len(data)), data):
        if i == 0 or i == len(data) - 1:
            continue
        else:
            line = d.split(',')
            if len(line) < 16:
                continue
            else:
                ret['data'][ret['header']['AF3']].append(float(line[1]))
                ret['data'][ret['header']['F7']].append(float(line[2]))
                ret['data'][ret['header']['F3']].append(float(line[3]))
                ret['data'][ret['header']['FC5']].append(float(line[4]))
                ret['data'][ret['header']['T7']].append(float(line[5]))
                ret['data'][ret['header']['P7']].append(float(line[6]))
                ret['data'][ret['header']['O1']].append(float(line[7]))
                ret['data'][ret['header']['O2']].append(float(line[8]))
                ret['data'][ret['header']['P8']].append(float(line[9]))
                ret['data'][ret['header']['T8']].append(float(line[10]))
                ret['data'][ret['header']['FC6']].append(float(line[11]))
                ret['data'][ret['header']['F4']].append(float(line[12]))
                ret['data'][ret['header']['F8']].append(float(line[13]))
                ret['data'][ret['header']['AF4']].append(float(line[14]))
    return ret
