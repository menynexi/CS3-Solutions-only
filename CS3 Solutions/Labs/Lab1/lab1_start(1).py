import numpy as np
import matplotlib.pyplot as plt
import time

def display_image(im,dpi = 160,figname='',save=True):
    height, width= im.shape[0], im.shape[1]
    figsize = width / float(dpi), height / float(dpi)
    fig, ax = plt.subplots(figsize=figsize)
    ax.imshow(im, cmap='gray')
    if figname!='':
        fig.suptitle(figname, fontsize=16)
        if save: fig.savefig(figname+'.jpg')

def copy_loops(im):
    im_copy = np.zeros((im.shape[0],im.shape[1],im.shape[2]))    
    for r in range(im.shape[0]):
        for c in range(im.shape[1]):
            for color in range(3):
                im_copy[r,c,color] =  im[r,c,color]
    return im_copy

def copy_slicing(im):
    # Build  copy using a single for loop. Note that im_copy = im would just copy the reference, not the actual array
    im_copy = np.zeros((im.shape[0],im.shape[1],im.shape[2]))
    for i in range(3): # Copy by color channel
        im_copy[:,:,i]= im[:,:,i]
    return im_copy
    
if __name__ == "__main__":
    
    plt.close('all')
    img = plt.imread('UTEP.JPG').astype(float)/255
    display_image(img,figname='original')

    start = time.time()
    img2 = copy_loops(img)
    end = time.time()
    time_loop = end - start
    print('Time to build image copy using loops: {:5.3f} seconds'.format(time_loop))
    display_image(img2,figname='copy 1')
    
    start = time.time()
    img3 = copy_slicing(img)
    end = time.time()
    time_slice = end - start
    print('Time to build image copy using slicing: {:5.3f} seconds'.format(time_slice))
    display_image(img3,figname='copy 2')
    print('Loop took {:5.3f} times as long as slicing'.format(time_loop/time_slice))
    print('Slicing saved {:5.2f}% of the time compared to loops'.format(100*(time_loop-time_slice)/time_loop))
    
    