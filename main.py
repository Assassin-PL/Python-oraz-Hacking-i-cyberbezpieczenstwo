from utlis import Stack, Queue
from kino import CinemaQueue, Customer

stack = Stack()

stack.push('A')
stack.push('B')
stack.push('C')

print("Stos pododaniu elementow: ", stack.pokaz_elemnty())

print("Usuniety element: ", stack.pop())

print("Ostatni element w stosie: ", stack.peek())

print("Stos po usunieciu elementu: ", stack.pokaz_elemnty())

print("Czy stos jest pusty: ", stack.is_empty())

print("Rozmiar stosu: ", stack.size())

kolejka = Queue()

kolejka.enqueue('A')
kolejka.enqueue('B')
kolejka.enqueue('C')

print("kolejka pododaniu elementow: ", kolejka.pokaz_elemnty())

print("Usuniety element: ", kolejka.dequeue())

print("Ostatni element w kolejce: ", kolejka.peek())

print("kolejka po usunieciu elementu: ", kolejka.pokaz_elemnty())

print("Czy kolejka jest pusta: ", kolejka.is_empty())

print("Rozmiar kolejki: ", kolejka.size())

# zadanie z kolejka do kina

queue = CinemaQueue()

queue.add_customer(Customer('Anna', 'popcorn'))
queue.add_customer(Customer('Tomasz', 'cola'))
queue.add_customer(Customer('marta', 'hot dog'))

while not queue.is_empty():
    customer : Customer = queue.remove_customer()
    print(f"Klient {customer.name} kupuje {customer.order}")

    if not queue.is_empty():
        next_order = queue.next_customer_order()
        print(f"Kolejny klient kupi {next_order}")