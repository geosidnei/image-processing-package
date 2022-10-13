#Author: Karina Tiemi Kato
#Revisor: Sidnei Lopes Ribeiro (13/10/2022)
# https://runebook.dev/pt/docs/scikit_image/api/skimage.io 

from skimage.io import imread, imsave

def read_image(path, is_gray = False):
    image = imread(path, as_gray = is_gray)
    return image

def save_image(image, path):
    imsave(path, image)
