# queues.py

from collections import deque

class FIFO:
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

fifo = FIFO ()
fifo.enqueue ("1st")
fifo.enqueue ("2nd")
fifo.enqueue ("3rd")

print (fifo)
print (fifo.dequeue ())
print (fifo.dequeue ())
print (fifo.dequeue ())
#print (fifo.dequeue ())

