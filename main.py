import numpy as np;

def print_arr():
    arr = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    print(f"tablica :\n {arr}")
    print(f"Pierwszy element: {arr[0]}")
    print(f"Ostatni element: {arr[-1]}")
    print(f"pierwszy zagniezdzony elemnt: {arr[0][0]}")
    print(f"Ostatni zagniezdzony element: {arr[-1][-1]}")
    print(f"typ tablicy: {type(arr)}")
    print(f"Ksztalt tablicy: {arr.shape}")
    return arr

def shapeShiffter(arr):
    print(f"tablica po zmianie ksztaltu na 1x9: \n {arr.reshape(1, 9)}")
    print(f"Ksztalt tablicy: {arr.shape}")
    print(f"tablica po zmianie ksztaltu na 9x1: \n {arr.reshape(9, 1)}")
    print(f"Ksztalt tablicy: {arr.shape}")
    print(f"tablica po zmianie ksztaltu na ?x9: \n {arr.reshape(-1, 9)}")
    print(f"Ksztalt tablicy: {arr.shape}")
    print(f"tablica po zmianie ksztaltu na ?x3: \n {arr.reshape(3, -1)}")
    print(f"Ksztalt tablicy: {arr.shape}")
    newarr = np.array_split(arr.reshape(-1, 9), 3)
    print(f"tablica po zmianie ksztaltu na 3x3: \n {newarr}")

def data_format():
    try:
        arr = np.array( [[1.1,2.2,3.3], ["kot",2,"pies"], ['a','b','c'] ],dtype='U')
        print(f"tablica z formatem danych: \n {arr}")
        print(f"typ tablicy: {type(arr)}")
    except Exception as e:
        print(f"Blad: {e}")

    arr = np.array([[-1.1,2.2,3.3],[1.1,2.2,3.3],[1.1,2.2,3.3]], dtype='U')
    print(f"tablica z formatem danych: \n {arr}")
    print(f"typ tablicy: {type(arr)}")
    arr = np.array([[-1.1,2.2,3.3],[1.1,2.2,3.3],[1.1,2.2,3.3]], dtype='int')
    print(f"tablica z formatem danych: \n {arr}")
    print(f"typ tablicy: {type(arr)}")
    arr = np.array([[-1.1,2.2,3.3],[1.1,2.2,3.3],[1.1,2.2,3.3]], dtype='?')
    print(f"tablica z formatem danych: \n {arr}")
    print(f"typ tablicy: {type(arr)}")

def sorted():                                     
    arr = np.array([[3,2,1],[6,5,4],[9,8,7]])
    print(f"tablica przed sortowaniem: \n {arr}")
    print(f"tablica po sortowaniu: \n {np.sort(arr)}")

def generate():
    arr = np.random.randint(10, size=(3, 3))
    print(f"tablica z losowymi liczbami: \n {arr}")

def get_random_items(arr):
    return np.random.choice(arr, size=(3, 3))
arr = print_arr()
shapeShiffter(arr)
data_format()
sorted()
generate()
picked = get_random_items(arr)