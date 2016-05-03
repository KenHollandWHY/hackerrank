'''
#[Ref]: http://stackoverflow.com/questions/4479463/using-fourier-analysis-for-time-series-prediction
Score: 50.29/100
'''
import numpy as np
from numpy import fft

def fourierExtrapolation(x, n_predict):
    n = x.size
    n_harm = 5                     # number of harmonics in model
    t = np.arange(0, n)
    p = np.polyfit(t, x, 1)         # find linear trend in x
    x_notrend = x - p[0] * t        # detrended x
    x_freqdom = fft.fft(x_notrend)  # detrended x in frequency domain
    f = fft.fftfreq(n)              # frequencies
    indexes = list(range(n))
    # sort indexes by frequency, lower -> higher
    indexes.sort(key = lambda i: np.absolute(f[i]))

    t = np.arange(0, n + n_predict)
    restored_sig = np.zeros(t.size)
    for i in indexes[:1 + n_harm * 2]:
        ampli = np.absolute(x_freqdom[i]) / n   # amplitude
        phase = np.angle(x_freqdom[i])          # phase
        restored_sig += ampli * np.cos(2 * np.pi * f[i] * t + phase)
    return restored_sig + p[0] * t


#load input sample data
session_data = []
N = int(input())
for i in range(N):
    session_data.append(int(input()))

x = np.array(session_data)

# predict per each day of the week
data_day_of_week = []
for day in range(7):
    extrapolation = fourierExtrapolation(x[day::7], 5)
    data_day_of_week.append(extrapolation)

data = []
for i in range(N+30):
    q, day = divmod(i,7)
    data.append(data_day_of_week[day][q])

for i in range(N,N+30):
    print(int(data[i]))

# draw graph
#import matplotlib.pyplot as plt
#plt.plot(np.arange(0, extrapolation.size), extrapolation, 'r', label = 'extrapolation')
#plt.plot(np.arange(0, x.size), x, 'b', label = 'x', linewidth = 2)
#plt.legend()
#plt.show()