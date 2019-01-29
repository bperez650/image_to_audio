import numpy as np
import matplotlib.image as ima
import matplotlib.pyplot as plt
import cv2
import numpy.ma as ma

img = cv2.imread("colorWheel.jpg",1)
imgA = img
imgB = img
imgC = img
#plt.imshow(img)
imga = np.zeros(img.shape)
imgb = np.zeros(img.shape)
imgc = np.zeros(img.shape)
fig = plt.figure(figsize= (8,8))

fig1 = fig.add_subplot(221)
imgA[:,:,1] = 0
imgA[:,:,0] = 0
imga = imgA
plt.imshow(imga)

fig2 = fig.add_subplot(222)
imgB[:,:,2] = 0
imgB[:,:,0] = 0
imgb = imgB
plt.imshow(imgb)

fig3 = fig.add_subplot(223)
imgC[:,:,2] = 0
imgC[:,:,1] = 0
imgc = imgC
plt.imshow(imgc)




# plt.figure(figsize=(5,5))
# plt.imshow(img2)
plt.show()



# cmap = " Reds_r"
imgshape = np.shape(img)
# dim1 = img[:,0,0]
# dim2 = img[0,:,0]
# dim3 = img[0,0,:]
#
# for index, row in enumerate(dim1):
#     for ind, column in enumerate(dim2):
#         a = img[index,ind]
#         #ax = ma.masked_array(a, mask=[0, 1, 1])
#         x = [0,0,1]
#         newImg = img[index, ind, x]




