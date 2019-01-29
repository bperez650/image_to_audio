import cv2
import numpy as np
from matplotlib import pyplot as plt
import struct as st

Fs = 44100  # sampling rate
Ts = 1.0/Fs # sampling interval
sinu = np.zeros(Fs) #create array of zeros
t2 = np.arange(0,1,Ts) # time vector

# read in image
img = cv2.imread('rembrant.jpg',0)
#current_row = img[0]
for row_count, row_value in enumerate(img):
    #if row_count < 10:
        current_row = row_value
        length = len(current_row)
        half_length = int(length/2) #take half of length
        t3 = np.arange(length)
        fourier = np.fft.fft(current_row) / length
        abs_fourier = abs(fourier)  # take magnitude of fourier eliminate the complex conjugate
        t1 = np.arange(half_length)    # plot only mag
        norm_fourier = abs_fourier[range(half_length)]

        #find components of fourier
        fo = open("hmm2.wav", "ab") #open file to write to
        for index, value in enumerate(abs_fourier):
            if value > .01:
                sinu += 2 * value * np.sin(2*np.pi*index*t2)

        # fig, ax = plt.subplots(3, 1)
        # ax[0].plot(t3, current_row)
        # ax[0].set_xlabel('Time')
        # ax[0].set_ylabel('Amplitude')
        # ax[1].plot(t1, norm_fourier, 'r')  # plotting the spectrum
        # ax[1].set_xlabel('Freq (Hz)')
        # ax[1].set_ylabel('|Y(freq)|')
        # ax[2].plot(t2, sinu)
        # ax[2].set_xlabel('Time')
        # ax[2].set_ylabel('Amplitude')
        #
        # plt.show()
        for i in sinu:
            fo.write(st.pack("f", i))



fo.close()