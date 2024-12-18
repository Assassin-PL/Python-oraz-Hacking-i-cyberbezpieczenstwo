from utlis import Stack

stack = Stack()

stack.push('A')
stack.push('B')
stack.push('C')

print("Stos pododaniu elementow: ", stack)

print("Usuniety element: ", stack.pop())

print("Ostatni element w stosie: ", stack.peak())

print("Stos po usunieciu elementu: ", stack)

print("Czy stos jest pusty: ", stack.is_empty())

print("Rozmiar stosu: ", stack.size())