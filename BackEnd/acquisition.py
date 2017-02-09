
import sys,os, shutil
import time
import glob


STATE0 = 'NEUTRAL'

STATE1 = 'UP'

STATE2 = 'DOWN'

STATE3 = 'RIGHT'

STATE4 = 'LEFT'

STATE5 = 'FORWARD'

STATE6 = 'BACKWARD'


STATE_FILES = [STATE0, STATE1, STATE2, STATE3, STATE4, STATE5, STATE6]


FOLDER_NAME = 'userdata'


def make_file_name(id, state_number):
    global FOLDER_NAME
    folder_path = FOLDER_NAME + '/' + id
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)
    file_path = ''
    i = 0
    while 1:
        file_path = folder_path + '/' + STATE_FILES[state_number] + '_' + id + '_' + str(i) + '.csv'
        if not os.path.isfile(file_path):
            break
        i += 1
    return file_path




def disconect_BCI():
    libEDK.EE_DataFree(hData)
    libEDK.EE_EngineDisconnect()
    libEDK.EE_EmoStateFree(eState)
    libEDK.EE_EmoEngineEventFree(eEvent)


def get_data(id='tu', state_number=0):
    data = [read_file(name) for name in glob.glob(FOLDER_NAME+'/' + id + '/' + STATE_FILES[state_number]+'_' + id +'_[0-9]*.csv')]
    return data

def reset_data(id):
    folder = "userdata/" + id
    classifier_folder = 'classifier'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print e
    for the_file in os.listdir(classifier_folder):
        file_path = os.path.join(classifier_folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print e

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
