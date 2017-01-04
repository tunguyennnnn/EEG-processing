import os.path
from sklearn.externals import joblib
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import acquisition as AQ
import feature_extraction as FE
from sklearn.feature_selection import RFE
import json
import glob

''' Manage File System For Classifiers'''
FOLDER_PATH = 'classifier'
CLASSIFIER_FILE_PREFIX = 'clf'


def get_classifier(id):
    ''' input: id of the user
        return a classifier corresponding to the id
        if there's no classifier with that id: create a new classifier and file
    '''
    file_name = FOLDER_PATH + "/" + CLASSIFIER_FILE_PREFIX + id + '.pkl'
    if classifier_exist(id):
        return joblib.load(file_name)
    else:
        return create_new_classifer(id)

def create_new_classifer(id):
    file_name = FOLDER_PATH + "/" + CLASSIFIER_FILE_PREFIX + id + '.pkl'
    newCF = LinearDiscriminantAnalysis();
    joblib.dump(newCF, file_name)
    return newCF

def classifier_exist(id):
    file_name = FOLDER_PATH + "/" + CLASSIFIER_FILE_PREFIX + id + '.pkl'
    return os.path.isfile(file_name)

def store(id, clf):
    file_name = FOLDER_PATH + "/" + CLASSIFIER_FILE_PREFIX + id + '.pkl'
    joblib.dump(clf, file_name)

def remove_classifier(id):
    file_name = FOLDER_PATH + "/" + CLASSIFIER_FILE_PREFIX + id + '.pkl'
    if classifier_exist(id):
        os.remove(file_name)
        return True
    return False


def train(id, training_data, training_classes):
    '''
        input: id of the user
               training_data: 2D array of data
               training_classes: 1D arrat of classes
        example of input:
        id: "tu"
        training_data: [[1,2], [2,3], [4,4], [2,2]]
        training_classes: [2,2,1,1]

    '''
    clf = get_classifier(id)
    clf.fit(training_data, training_classes)
    store(id, clf)
    return True

def predict(id, target_data):
    '''
        input: id of the user
        target_data: data used to predict classes
        return None if no classifer is found, otherwise return its class
    '''
    if classifier_exist(id):
        clf = get_classifier(id)
        return clf.predict(target_data)[0]


def pre_train(list_of_data, list_of_commands):

    classifiers = [LinearDiscriminantAnalysis() for i in range(14)]
    selectors = [RFE(LinearDiscriminantAnalysis(), 10, step=1) for i in range(14)]

    for index in range(14):
        training_data = []
        target_classes = []
        for command, command_data in zip(list_of_commands, list_of_data):
            print command
            for i in xrange(100, len(command_data[index]) - 100, 50):
                try:
                    training_data.append(FE.compute_feature_vector(command_data[index][i: i + 100]))
                    target_classes.append(command)
                except:
                    continue
        classifiers[index].fit(training_data, target_classes)
        selectors[index].fit(training_data, target_classes)
    return (classifiers, selectors)

def evaluate_classifiers(list_of_classifers, list_of_selectors, list_of_data, list_of_commands):
    CHANNELS = ['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7','O1', 'O2', 'P8', 'T8', 'FC6', 'F4','F8', 'AF4']
    channel_results = []
    for index in range(14):
        total = 0
        classifier_accuracy = 0
        selector_accuracy = 0
        detail_results = {}
        for command, command_data in zip(list_of_commands, list_of_data):
            command_total = 0
            command_cf_accuracy = 0
            command_sl_accuracy = 0
            for i in xrange(50, len(command_data[index])- 50, 100):
                total += 1
                command_total += 1
                try:
                    feature_vector = FE.compute_feature_vector(command_data[index][i: i + 100])
                    if list_of_classifers[index].predict(feature_vector)[0] == command:
                        command_cf_accuracy += 1
                        classifier_accuracy += 1
                    if list_of_selectors[index].predict(feature_vector)[0] == command:
                        command_sl_accuracy +=1
                        selector_accuracy += 1
                except:
                    continue
            detail_results[command] = {}
            detail_results[command]['clf'] = float(command_cf_accuracy)/ float(command_total)
            detail_results[command]['sl'] = float(command_sl_accuracy)/ float(command_total)
        if classifier_accuracy > selector_accuracy:
            for command in detail_results:
                detail_results[command] = detail_results[command]['clf']
            channel_results.append({'cf': list_of_selectors[index], 'channel': CHANNELS[index], 'type': 'classifier', 'accuracy': (float(classifier_accuracy)/float(total)), 'command_detail': detail_results})
        else:
            for command in detail_results:
                detail_results[command] = detail_results[command]['sl']
            channel_results.append({'cf': list_of_selectors[index], 'channel': CHANNELS[index], 'type': 'selector', 'accuracy': (float(selector_accuracy)/float(total)), 'command_detail': detail_results})

    channel_results.sort(key=lambda x: x["accuracy"], reverse=True)
    return channel_results


def channel_selection(list_of_classifers):
    selected_classifiers = []
    for classifier in list_of_classifers:
        average = classifier['accuracy']
        take = True
        for command in classifier['command_detail']:
            if abs(average - classifier['command_detail'][command]) > 0.15:
                take = False
                break
        if take:
            selected_classifiers.append(classifier)
    return selected_classifiers


def training(id, list_of_commands):
    training_data = []
    testing_data = []
    for command in list_of_commands:
        command_data = AQ.get_data(id, command)
        command_train_data = [[] for i in range(14)]
        command_test_data = [[] for i in range(14)]
        for sample in command_data:
            train, test = AQ.split_data_for_training(sample['data'])
            for i in range(14):
                command_train_data[i] += train[i]
                command_test_data[i] += test[i]
        training_data.append(command_train_data)
        testing_data.append(command_test_data)

    classifiers, selectors = pre_train(training_data, list_of_commands)
    results = evaluate_classifiers(classifiers, selectors, testing_data, list_of_commands)
    print results
    store_classifier_profiles(id,results)


def store_classifier_profiles(id, clfs):
    channel_info = {}
    for i, clf in zip(range(len(clfs)), clfs):
        channel_info[clf['channel']] = {}
        channel_info[clf['channel']]['accuracy'] = clf['accuracy']
        channel_info[clf['channel']]['detail'] = clf['command_detail']
        file_name = FOLDER_PATH + '/' + id + '_' + clf['channel'] + '.pkl'
        joblib.dump(clf['cf'], file_name)
    channel_info_file = FOLDER_PATH + '/' + id + '.txt'
    file(channel_info_file, 'w')
    f = open(channel_info_file , 'w')
    print >> f, json.dumps(channel_info)
    f.close()

def get_classifiers(id):
    channel_info_file = FOLDER_PATH + '/' + id + '.txt'
    channel_info = json.loads(open(channel_info_file, 'r').read())
    classifiers = []
    for name in glob.glob(FOLDER_PATH +'/' + id + '_' + '*' + '.pkl'):
        channel = name.split('_')[1].split('.')[0]
        accuracy =  channel_info[channel]['accuracy']
        detail = channel_info[channel]['detail']
        cf = joblib.load(name)
        classifiers.append({'cf': cf, 'channel': channel, 'accuracy': accuracy, 'detail': detail})
    return classifiers
