#pip install imageio
#pip install matplotlib
#pip install scipy

img = "https://i.postimg.cc/8C9XkVkH/73515599-1283555595165990-4504959714664120320-o.jpg" #rabid

img = "https://i.postimg.cc/mr1NwXCp/50570646-2729587910600609-505289888623493120-o-jpg-nc-cat-110-ccb-2-nc-sid-85a577-nc-ohc-De-Zh-Rdnv.jpg" #iftekhar

img = "https://i.postimg.cc/XJ0FgVVX/79154490-1199177676946749-8941037426734792704-n-jpg-nc-cat-107-ccb-2-nc-sid-85a577-nc-ohc-i1-DRk1n.jpg" #fahim

img = "https://i.postimg.cc/s2nxMsvt/91192509-2568584790048337-8494390995801079808-n.jpg" #maisha

def dodge(front,back):
    result=front*255/(255-back) 
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

import numpy as np
def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


import imageio
s = imageio.imread(img)
g=grayscale(s)
i = 255-g
import scipy.ndimage
b = scipy.ndimage.filters.gaussian_filter(i,sigma=30) #dark hobe sigma barale
r= dodge(b,g)


import matplotlib.pyplot as plt
plt.imshow(r, cmap="gray")


plt.imsave('img4.png', r, cmap='gray', vmin=0, vmax=255)