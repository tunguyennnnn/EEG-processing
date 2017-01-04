import numpy as np
import pywt
from math import *
from pylab import plot, log10, linspace, axis
from spectrum import *


''' Feature extraction functions'''
def root_mean_square(signal):
    return sqrt(sum(n*n for n in signal)/len(signal))

def mean_absolute_value(signal):
    return integrated_eeg(signal)/len(signal)

def integrated_eeg(signal):
    return sum(abs(n) for n in signal)

def simple_square_integral(signal):
    return sum(n*n for n in signal)

def var(signal):
    return simple_square_integral(signal)/(len(signal) - 1)

def average_amplitude_change(signal):
    sum = 0.0
    for i in range(len(signal) - 1):
        sum += abs(signal[i + 1] - signal[i])
    return sum/len(signal)


''' Wave let feature extractions'''

def compute_wavelet(signal, depth=4):
    wavelet_info = []
    cA, cD = pywt.dwt(signal, 'db4')
    for i in range(depth-1):
        cA1, cD = pywt.dwt(cA, 'db4')
        wavelet_info.append(cD)
        if i == depth - 1:
            break
        else:
            cA = cA1
    return wavelet_info


def compute_burg_params(data, order=6):
    AR, P, k = arburg(data, order)
    return [np.absolute(x) for x in AR]

def build_wavelet_feature_vector(signal):
    ''' input: 1D array
        output: 2D array wavelet feature matrix
    '''
    burg_params = compute_burg_params(signal)
    wavelets = compute_wavelet(signal)
    #wavlet_features =
    return np.array([[root_mean_square(wavelet), mean_absolute_value(wavelet), integrated_eeg(wavelet), simple_square_integral(wavelet), var(wavelet), average_amplitude_change(wavelet)] for wavelet in wavelets])
