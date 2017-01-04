import preprocessing as PR
import feature_extraction as FE
import eeg_classification as CF
import scipy.io as sio
import numpy as np
from sklearn import svm
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt

length = 190590
training_length = 171530
test_legnth = length - training_length
data1 = np.array(sio.loadmat('BCICIV_calib_ds1a.mat')['cnt']).T[1]
data2 = np.array(sio.loadmat('BCICIV_eval_ds1g.mat')['cnt']).T[1]


training1, test1 = data1[0: training_length], data1[training_length: -1]
training2, test2 = data2[0: training_length], data2[training_length: -1]

plt.figure()

plt.subplot(2, 1, 1)
plt.plot(training1[:1000])
plt.subplot(2,1,2)
plt.plot(training2[:1000])
plt.show()
# clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(10, 3), random_state=1)
#
# for i in xrange(0, training_length - 100, 100):
#     d1 = training1[i: i + 100]
#     d2 = training2[i: i + 100]
#     f1 = FE.build_wavelet_feature_vector(d1).flatten()
#     f2 = FE.build_wavelet_feature_vector(d2).flatten()
#     clf.fit([f1, f2], ["1", "2"])
#
#
# for i in xrange(0, test_legnth - 100, 100):
#     d1 = test1[i: i + 100]
#     d2 = test2[i: i + 100]
#     f1 = FE.build_wavelet_feature_vector(d1).flatten()
#     f2 = FE.build_wavelet_feature_vector(d2).flatten()
#     print "1 %s" % clf.predict(f1)
#     print "2 %s" % clf.predict(f2)
