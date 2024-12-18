from utlis import Queue
class Customer:
    def __init__(self, name: str, order: str):
        self.name = name
        self.order = order
class CinemaQueue():
    def __init__(self):
        self.queue = Queue() 
    def is_empty(self):
        return self.queue.is_empty()
    def add_customer(self, customer: Customer):
        self.queue.enqueue(customer)
    def remove_customer(self):
        return self.queue.dequeue()
    def next_customer_order(self):
        if not self.is_empty():
            next_customer : Customer = self.queue.peek()
            return next_customer.order
        