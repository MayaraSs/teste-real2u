import os
import cv2
import numpy as np
import urllib.request

def download_image2(url):
    urllib.request.urlretrieve(url)

def download_image(url):
   os.system('wget {}'.format(url))

def open_image(name):
    img = cv2.imread(name)
    return img

def apply_filter_blur(img):
    gaussianBlurKernel = np.array(([[1, 2, 1], [2, 4, 2], [1, 2, 1]]), np.float32)/9
    gaussianBlur = cv2.filter2D(src=img, kernel=gaussianBlurKernel, ddepth=-1)
    return gaussianBlur

def apply_filter(img, filter_to_apply):
    """
      This functions will be apply filter to image: img
    """
    image_with_filter = cv2.filter2D(src=img, kernel=filter_to_apply, ddepth=-1)
    return image_with_filter


def show_img(img):
    cv2.imshow('Image ', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

def save_image(name_to_save, img):
    cv2.imwrite(name_to_save, img)

def get_image_name(url):
    url_splited = url.split('/')
    for item in url_splited:
        if '.jpg' in item:
            return item

#image_name = get_image_name('http://site.meishij.net/r/58/25/3568808/a3568808_142682562777944.jpg')
#print(image_name)
#download_image('http://site.meishij.net/r/58/25/3568808/a3568808_142682562777944.jpg')
"""img = open_image('a3568808_142682562777944.jpg')
img_with_blur = apply_filter_blur(img)
save_image("image_antiga.jpg", img)
save_image("image_com_filtro.jpg", img_with_blur)

show_img(img_with_blur)
show_img(img)


hahaha = np.array(([[1, 2, 21], [2, 4, 2], [12, 2, 1]]), np.float32)/9
image_with_filter = apply_filter(img, hahaha)
show_img(image_with_filter)"""
