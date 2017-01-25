from scipy.signal import butter, lfilter
from sklearn.decomposition import FastICA

CHANNELS = ["AF3", "F7", "F3", "FC5", "T7", "P7", "O1", "O2", "P8", "T8", "FC6", "F4", "F8", "AF4"]

def butter_bandpass(lowcut, highcut, fs=128, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


def filter_noise(signals, num_of_components = 14):
    ica = FastICA(n_components= num_of_components)
    return ica.fit_transform(signals).T
