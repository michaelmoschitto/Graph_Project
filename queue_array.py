
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.num_items = 0
        self.back = 0
        self.front = 0
        self.items = [None]*capacity

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        return self.size() == 0


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        return self.size() == self.capacity


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if not self.is_full():
            if self.back == self.capacity-1:
                self.items[0] = item
                self.back = 0
            else:
                if self.size() == 0:
                    self.items[0] = item
                else:
                    self.back += 1
                    self.items[self.back] = item
            self.num_items += 1
        else:
            raise IndexError("Unable to enqueue. Queue Full")
                


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if not self.is_empty():
            if self.front == self.capacity-1:
                dequeueItem = self.items[self.front]
                self.front = 0
                self.num_items -= 1
                return dequeueItem
            dequeueItem = self.items[self.front]
            self.num_items -=1
            if self.size() == 0:
                self.front = 0
                self.back = 0
            else:
                self.front += 1
            return dequeueItem
        
        else:
            raise IndexError("Unable to dequeue. Queue Empty")


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items
