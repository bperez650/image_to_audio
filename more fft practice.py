import matplotlib.pyplot as plt
import numpy as np
import cv2


sampFreq = 8000 #sampling frequency
period  = 1/sampFreq
timeV = np.arange(0,1,period)
length = len(timeV)

freq1 = 1
#freq2 = 3

sin1 = 1* np.sin(2 * np.pi * freq1 * timeV) #+ 2*np.sin(2*np.pi*freq2*timeV)
t = sin1.dtype

plt.figure()
fig1 = plt.subplot(221)
fig1.plot(sin1,"ro")

halfLength = int(length / 2)
fourier = np.fft.fft(sin1) / length
absFourier = abs(fourier)
normFourier = absFourier[range(halfLength)]

fig2 = plt.subplot(222)
fig2.plot(normFourier,"bo")

for freqComponent, value in enumerate(normFourier):
    if value > .1:
        audioSine = (2 * value) * np.sin(2 * np.pi * freqComponent * timeV)

fig3 = plt.subplot(223)
fig3.plot(audioSine, "bo")

plt.show()

# with open("testSinu.wav","wb") as file:
#     for value in sin1:
#         file.write(value)

