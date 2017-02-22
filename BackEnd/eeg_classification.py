import os.path
from sklearn.externals import joblib
from sklearn import svm
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import acquisition as AQ
import feature_extraction as FE
from sklearn.feature_selection import RFE
import json
import glob
import numpy as np
import signal_similarity as sim
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
    sim_obj = sim.Similarity()
    for index in range(14):
        training_data = []
        target_classes = []
        training_d = [[] for i in range(len(list_of_commands))]

        for ind, command, command_data in zip(range(len(list_of_commands)), list_of_commands, list_of_data):
            print command
            for i in xrange(100, len(command_data[index]) - 100, 50):
                try:
                    training_d[ind].append(FE.compute_feature_vector(command_data[index][i: i + 100]))
                except:
                    continue
            for i in xrange(100, len(command_data[index]) - 200, 50):
                try:
                    training_d[ind].append(FE.compute_feature_vector(command_data[index][i: i+200]))
                except:
                    continue
        min_length = min([len(d) for d in training_d])
        for i in range(min_length):
            for command, d in zip(list_of_commands, training_d):
                training_data.append(d[i])
                target_classes.append(command)
        classifiers[index].fit(training_data, target_classes)
        selectors[index].fit(training_data, target_classes)
    return (classifiers, selectors)

def pre_train_svm(list_of_data, list_of_commands):
    classifier = svm.SVC()
    selector = RFE(svm.SVC())
    min_len = len(list_of_data[0][0])
    for data in list_of_data:
        if len(data[0]) < min_len:
            min_len = len(data[0])

    for i in xrange(0, min_len, 50):
        training_data = []
        for data in list_of_data:
            training_d = np.array([d[i: i+100] for d in data])
            try:
                feature_vector = FE.compute_ff_feature_vector(training_d.T, 128)
                feature_vector = np.nan_to_num(feature_vector)
                training_data.append(feature_vector.tolist())
            except:
                print "error"
        classifier.fit(training_data, list_of_commands)
    return classifier, classifier

def evaluate_svm(classifier, testing_data, list_of_commands):
    min_len = len(testing_data[0][0])
    for data in testing_data:
        if len(data[0]) < min_len:
            min_len = len(data[0])
    total = 0.0
    correct = 0.0
    for i in xrange(0, min_len, 50):
        for command, data in zip(list_of_commands, testing_data):
            testing_d = np.array([d[i: i + 100] for d in data])
            feature_vector = FE.compute_ff_feature_vector(testing_d.T, 128)
            total += 1
            if classifier.predict(feature_vector)[0] == command:
                correct = 1
    return {'clf': classifier, 'accuracy': (correct/total)}

def evaluate_classifiers(list_of_classifers, list_of_selectors, list_of_data, list_of_commands):
    CHANNELS = ['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7','O1', 'O2', 'P8', 'T8', 'FC6', 'F4','F8', 'AF4', 'COMBINED']
    channel_results = []
    for index in range(15):
        total = 0
        classifier_accuracy = 0
        selector_accuracy = 0
        detail_results = {}
        for command, command_data in zip(list_of_commands, list_of_data):
            command_total = 0
            command_cf_accuracy = 0
            command_sl_accuracy = 0
            if index == 14:
                for i in xrange(50, len(command_data[0]) - 50, 50):
                    total += 1
                    command_total += 1
                    tested_data = np.array([data[i: i+100] for data in command_data])
                    feature_vector = FE.compute_ff_feature_vector(tested_data.T, 128)
                    feature_vector = np.nan_to_num(feature_vector)
                    if list_of_classifers[index].predict(feature_vector)[0] == command:
                        command_cf_accuracy += 1
                        classifier_accuracy += 1
                    if list_of_selectors[index].predict(feature_vector)[0] == command:
                        command_sl_accuracy +=1
                        selector_accuracy += 1
            else:
                for i in xrange(50, len(command_data[index])- 50, 50):
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

def generate_new_classifiers(selected_classifiers, training_data, testing_data, list_of_commands):
    CHANNELS = ['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7','O1', 'O2', 'P8', 'T8', 'FC6', 'F4','F8', 'AF4']
    sum_classifier = LinearDiscriminantAnalysis()
    channels = [CHANNELS.index(clf_info['channel']) for clf_info in selected_classifiers]
    name = "-".join([clf_info['channel'] for clf_info in selected_classifiers])
    sum_training_data = []
    for data in training_data:
        sum_data = np.array([0.0 for i in range(len(data[0]))])
        for i in channels:
            sum_data += np.array(data[i])
        sum_training_data.append(sum_data)

    training_features = []
    training_classes = []
    for index, command in zip(range(len(list_of_commands)), list_of_commands):
        for i in xrange(100, len(sum_training_data[index]) - 100, 50):
            try:
                training_features.append(FE.compute_feature_vector(sum_training_data[index][i: i+100]))
                training_classes.append(command)
            except:
                continue
        for i in xrange(100, len(sum_training_data[index]) - 200, 50):
            try:
                training_features.append(FE.compute_feature_vector(sum_training_data[index][i: i+200]))
                training_classes.append(command)
            except:
                continue
    sum_classifier.fit(training_features, training_classes)
    detail = {}
    for command in list_of_commands:
        detail[command] = 1.0
    return {'cf': sum_classifier, 'channel': name, 'type': 'classifier', 'accuracy': 1.0, 'command_detail': detail}




def channel_selection(list_of_classifers):
    selected_classifiers = []
    for classifier in list_of_classifers:
        average = classifier['accuracy']
        print classifier['channel']
        print average
        take = True
        if average < 0.7 or classifier['channel'] == 'COMBINED':
            take = False
        else:
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
    combined_classifier, combined_selector = pre_train_svm(training_data, list_of_commands)
    classifiers.append(combined_classifier)
    selectors.append(combined_selector)
    results = channel_selection(evaluate_classifiers(classifiers, selectors, testing_data, list_of_commands))
    results.append(generate_new_classifiers(results, training_data, testing_data, list_of_commands))
    print results
    store_classifier_profiles(id,results)


def store_classifier_profiles(id, clfs):
    channel_info = {}
    for i, clf in zip(range(len(clfs)), clfs):
        print clf['channel']
        channel_info[clf['channel']] = {}
        channel_info[clf['channel']]['accuracy'] = clf['accuracy']
        channel_info[clf['channel']]['detail'] = clf['command_detail']
        file_name = FOLDER_PATH + '/' + id + '/' + id + '_' + clf['channel'] + '.pkl'
        joblib.dump(clf['cf'], file_name)
    channel_info_file = FOLDER_PATH + '/' + id + '/' + id + '.txt'
    file(channel_info_file, 'w')
    f = open(channel_info_file , 'w')
    print >> f, json.dumps(channel_info)
    f.close()

def get_classifiers(id):
    channel_info_file = FOLDER_PATH + '/' + id + '/' + id + '.txt'
    channel_info = json.loads(open(channel_info_file, 'r').read())
    classifiers = []
    for name in glob.glob(FOLDER_PATH +'/' + id + '/' + id + '_' + '*' + '.pkl'):
        channel = name.split('_')[1].split('.')[0]
        accuracy =  channel_info[channel]['accuracy']
        detail = channel_info[channel]['detail']
        cf = joblib.load(name)
        classifiers.append(ClassifierInfo(accuracy=accuracy, clf=cf, channel_name=channel, detail=detail))
    classifiers.sort(key=lambda x: x.accuracy, reverse=True)
    return classifiers

class ClassifierInfo:
    def __init__(self, accuracy=0.0, clf=LinearDiscriminantAnalysis(), channel_name='', detail = {}):
        self.accuracy = accuracy
        self.clf = clf
        self.channel = channel_name
        self.detail = detail

    def compute_probability(self, data):
        try:
            result = self.clf.predict(FE.compute_feature_vector(data))[0]
            return (result, self.detail[str(result)])
        except:
            return (0, 0)

def final_command(classifier_infos, channels_data):
    CHANNELS = ['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7','O1', 'O2', 'P8', 'T8', 'FC6', 'F4','F8', 'AF4', 'COMBINED']
    cls_info = None
    for cf in classifier_infos:
        if "-" in cf.channel:
            cls_info = cf
            break
        else:
            continue
    data = np.array([0.0 for i in channels_data[0]])
    for chan in cls_info.channel.split("-"):
        data += np.array(channels_data[CHANNELS.index(chan)])
    command, prediction = cls_info.compute_probability(data)
    return (command, prediction)
    #results = {}
    # for c_i in classifier_infos:
    #     if "-" in c_i.channel:
    #         data = np.array([0.0 for i in channels_data[0]])
    #         for chan in c_i.channel.split("-"):
    #             data += np.array(channels_data[CHANNELS.index(chan)])
    #     else:
    #         data = channels_data[CHANNELS.index(c_i.channel)]
    #     command, prediction = c_i.compute_probability(data)
    #     if results.has_key(command):
    #         results[command] += prediction
    #     else: results[command] = prediction
    # print results
    # command = -1
    # result = 0
    # for res in results.keys():
    #     if result < results[res]:
    #         result = results[res]
    #         command = res
    # return (command, result)
