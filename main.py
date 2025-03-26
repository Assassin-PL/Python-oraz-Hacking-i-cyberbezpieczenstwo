import cv2
from PIL import Image
import numpy as np

def show_image(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def read_image_cv(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    print(img)
    print(img.shape)
    print(img.dtype)
    return img

def read_image__PILO(path):
    img = Image.open(path)
    try:    
        print(img)
        print(img.size)
        print(img.mode)
    except:
        print(type(img))
    img.show()
    return img

image = read_image_cv('image.jpg')
# image2 = read_image__PILO('image.jpg')

def reverse_image(img):
    new_img = []
    for row in range(img.shape[0]):
        new_row = []
        for column in range(img.shape[1]):
            new_row.append(img[-1-row][column])
        new_img.append(new_row)
    return np.array(new_img)

show_image(reverse_image(image))