from fifo import FIFO

fifo = FIFO ()
fifo.enqueue ("1st")
fifo.enqueue ("2nd")
fifo.enqueue ("3rd")

print (fifo)
print (fifo.dequeue ())
print (fifo.dequeue ())
print (fifo.dequeue ())
#print (fifo.dequeue ())

