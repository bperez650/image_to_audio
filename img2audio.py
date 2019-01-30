import matplotlib.pyplot as plt
import numpy as np
import cv2

audioSine = 0
sampFreq = 8000 #sampling frequency
period = 1 / sampFreq
timeV = np.arange(0,1,period)

img = cv2.imread('rembrant.jpg',0)

columnSize = len(img)

for row in img[range(0,columnSize,10)]:
    rowLength = len(row)
    HalfRowLength = int(rowLength / 2)
    fourier = np.fft.fft(row) / rowLength
    absFourier = abs(fourier)
    normFourier = absFourier[range(HalfRowLength)]

    # plt.figure()
    # fig1 = plt.subplot(211)
    # fig1.plot(normFourier, "go")

    for freqComponent, value in enumerate(normFourier[range(10)]):
        if value > .1:
            audioSine += (2 * value) * np.sin(2 * np.pi * freqComponent * timeV)

    # fig2 = plt.subplot(212)
    # fig2.plot(audioSine, "b")
    # plt.show()

    # plt.figure()
    # plt.plot(audioSine, "bo")
    # plt.show()

    ma = max(audioSine)
    normAudioSine = audioSine / ma

    with open("testSinu.wav","ab") as file:
        for value in normAudioSine:
            file.write(value)

# plt.figure()
# plt.plot(audioSine, "bo")
# plt.show()