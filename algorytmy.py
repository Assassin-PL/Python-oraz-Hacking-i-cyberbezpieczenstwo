# Tu beda algorytmy na operacje na zbiorach danych
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
# zadanie utwurzcie tutaj liste losowych numerow, o dlugosci 20 elementow
# i z zakresu od 1 do 100

my_list = []

# wasz kod
for i in range(20):
    my_list.append(random.randint(1, 100))

print(my_list)

print ("Lista po sortowaniem: ")
bubble_sort(my_list)
print(my_list)