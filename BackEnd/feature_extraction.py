import numpy as np
import pywt
from math import *
from pylab import plot, log10, linspace, axis
from spectrum import *


''' Feature extraction functions'''
def mean_absolute_value(wavelet_coefficient):
    n = len(wavelet_coefficient)
    return sum([abs(x) for x in wavelet_coefficient])/n

def standard_deviation(wavelet_coefficient):
    return np.std(wavelet_coefficient)

def ratio_of_absolute_mean(wavelet_coefficient, adjacent):
    return mean_absolute_value(wavelet_coefficient)/mean_absolute_value(adjacent)

def average_power(wavelet_coefficient):
    n = len(wavelet_coefficient)
    return sum([x for x in wavelet_coefficient])/n


def compute_wavelet(array_data, depth=5):
    wavelet_info = []
    cA, cD = pywt.dwt(array_data, 'db4')
    for i in range(depth-1):
        cA1, cD = pywt.dwt(cA, 'db4')
        wavelet_info.append(cD)
        if i == depth - 1:
            wavelet_info.append(cA1)
        else:
            cA = cA1
    return wavelet_info

def compute_burg_params(signal, order=6):
    AR, P, k = arburg(signal, order)
    return [np.absolute(x) for x in AR]

def compute_feature_vector(signal):
    burg_params = compute_burg_params(signal)
    wavelet_coefficients = compute_wavelet(signal)
    n = len(wavelet_coefficients)
    feature_vector=[]
    for i, wc in zip(range(n), wavelet_coefficients):
        if i >= 2:
            feature_vector.append([mean_absolute_value(wc), average_power(wc), standard_deviation(wc), ratio_of_absolute_mean(wc, wavelet_coefficients[-1])])
    feature_vector.append(burg_params)
    return [x for sublist in feature_vector for x in sublist]
