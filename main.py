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

def  reverse_image_short(img):
    return img[::-1]

# show_image(reverse_image(image))
# show_image(reverse_image_short(image))
# show_image(cv2.flip(image, 0))

def gray_image(img):
    for row in range(img.shape[0]):
        for column in range(img.shape[1]):
            gray = int (sum(img[row][column]) / 3)
            img[row][column] = [gray, gray, gray]
    return img

# show_image(gray_image(image))
# show_image(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))

def sepia(img):
    for row in range(img.shape[0]):
        for column in range(img.shape[1]):
            B = img[row][column][0]
            G = img[row][column][1]
            R = img[row][column][2]
            img[row][column][0] = min(255, int(0.272*R + 0.534*G + 0.131*B))
            img[row][column][1] = min(255, int(0.349*R + 0.686*G + 0.168*B))
            img[row][column][2] = min(255, int(0.393*R + 0.769*G + 0.189*B))
    return np.array(img)

show_image(sepia(image))