import numpy as np
import pywt
from math import *
from pylab import plot, log10, linspace, axis
from spectrum import *
from scipy.fftpack import fft
import matplotlib.pyplot as plt
import pyeeg

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
            feature_vector += [mean_absolute_value(wc), average_power(wc), standard_deviation(wc), ratio_of_absolute_mean(wc, wavelet_coefficients[-1])]
    feature_vector += burg_params
    # power, power_ratio = pyeeg.bin_power(signal, [7, 12, 30], 128)
    # feature_vector += power_ratio.tolist()
    return feature_vector

'''FFT'''

def plot_wavelet(wavelets):
    plt.figure()
    length = len(wavelets)
    for i, wavelet in zip(length, wavelets):
        plt.subplot(length, 1, i + 1)
        plt.plot(wavelet)
    plt.figure()


def compute_ff_feature_vector(eegdata, Fs):
    """Extract the features from the EEG
        Inputs:
          eegdata: array of dimension [number of samples, number of channels]
          Fs: sampling frequency of eegdata
        Outputs:
          feature_vector: [number of features points; number of different features
    """

    # 1. Compute the PSD
    winSampleLength, nbCh = eegdata.shape

    # Apply Hamming window
    w = np.hamming(winSampleLength)
    dataWinCentered = eegdata - np.mean(eegdata, axis=0) # Remove offset
    dataWinCenteredHam = (dataWinCentered.T*w).T

    NFFT = nextpow2(winSampleLength)
    Y = np.fft.fft(dataWinCenteredHam, n=NFFT, axis=0)/winSampleLength
    PSD = 2*np.abs(Y[0:NFFT/2,:])
    f = Fs/2*np.linspace(0,1,NFFT/2)

    # SPECTRAL FEATURES
    # Average of band powers
    # Delta <4
    ind_delta, = np.where(f<4)
    meanDelta = np.mean(PSD[ind_delta,:],axis=0)
    # Theta 4-8
    ind_theta, = np.where((f>=4) & (f<=8))
    meanTheta = np.mean(PSD[ind_theta,:],axis=0)
    # Low alpha 8-10
    ind_alpha, = np.where((f>=8) & (f<=10))
    meanLowAlpha = np.mean(PSD[ind_alpha,:],axis=0)
    # Medium alpha
    ind_alpha, = np.where((f>=9) & (f<=11))
    meanMedAlpha = np.mean(PSD[ind_alpha,:],axis=0)
    # High alpha 10-12
    ind_alpha, = np.where((f>=10) & (f<=12))
    meanHighAlpha = np.mean(PSD[ind_alpha,:],axis=0)
    # Low beta 12-21
    ind_beta, = np.where((f>=12) & (f<=21))
    meanLowBeta = np.mean(PSD[ind_beta,:],axis=0)
    # High beta 21-30
    ind_beta, = np.where((f>=21) & (f<=30))
    meanHighBeta = np.mean(PSD[ind_beta,:],axis=0)
    # Alpha 8 - 12
    ind_alpha, = np.where((f>=8) & (f<=12))
    meanAlpha = np.mean(PSD[ind_alpha,:],axis=0)
    # Beta 12-30
    ind_beta, = np.where((f>=12) & (f<=30))
    meanBeta = np.mean(PSD[ind_beta,:],axis=0)

    feature_vector = np.concatenate((meanDelta, meanTheta, meanLowAlpha, meanHighAlpha,
                                     meanLowBeta, meanHighBeta,
                                     meanDelta/meanBeta, meanTheta/meanBeta,
                                     meanAlpha/meanBeta, meanAlpha/meanTheta),axis=0)

    feature_vector = np.log10(feature_vector)

    return feature_vector

def feature_names(ch_names):
    """
        Generate the name of the features

        Arguments
    ch_names: List with Electrode names
    """

    bands = ['pwr-delta', 'pwr-theta', 'pwr-low-alpha', 'pwr-high-alpha',
             'pwr-low-beta', 'pwr-high-beta',
             'pwr-delta/beta', 'pwr-theta/beta', 'pwr-alpha/beta', 'pwr-alpha-theta']
    feat_names = []
    for band in bands:
        for ch in range(0,len(ch_names)-1):
        #Last column is ommited because it is the Status Channel
            feat_names.append(band + '-' + ch_names[ch])

    return feat_names

def nextpow2(i):
    """ Find the next power of 2 for number i """
    n = 1
    while n < i:
        n *= 2
    return n
