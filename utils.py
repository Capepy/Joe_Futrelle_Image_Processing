import tempfile
from IPython.core import display

from matplotlib import pyplot as plt

from skimage.io import imread, imsave
from skimage import img_as_float, img_as_ubyte

def _show_arr(arr):
    with tempfile.NamedTemporaryFile(suffix='.png') as tf:
        imsave(tf.name,arr)
        return display.Image(filename=tf.name)

def show_image(arr):
    return _show_arr(img_as_ubyte(img_as_float(arr)))

def show_mask(arr):
    return _show_arr((arr>0)*255)

def show_channels(rgb):
    fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=(15, 5), sharex=True, sharey=True)
    ax1.imshow(rgb[:,:,0],cmap='gray')
    ax1.set_adjustable('box-forced')
    ax2.imshow(rgb[:,:,1],cmap='gray')
    ax2.set_adjustable('box-forced')
    ax3.imshow(rgb[:,:,2],cmap='gray')
    ax3.set_adjustable('box-forced')

