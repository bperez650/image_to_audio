import matplotlib.pyplot as plt
import numpy as np
import cv2

audioSine = 0
sampFreq = 8000 #sampling frequency
period  = 1/sampFreq
timeV = np.arange(0,1,period)

img = cv2.imread('rembrant.jpg',0)

for row in img:
    length = len(row)
    halfLength = int(length / 2)
    fourier = np.fft.fft(row) / length
    absFourier = abs(fourier)
    normFourier = absFourier[range(halfLength)]

    for freqComponent, value in enumerate(normFourier):
        if value > .1:
            audioSine += (2 * value) * np.sin(2 * np.pi * freqComponent * timeV)

    plt.figure()
    plt.plot(audioSine, "bo")

    plt.show()

with open("testSinu.wav","wb") as file:
    for value in audioSine:
        file.write(value)

