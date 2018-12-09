##### Notes of part 2

I initially attempted using array slicing to reuse as much of the part 1 solution as possible. I did this because array slicing is
advertised as the equivalent of `system.arraycopy` is Java. While it is functionally equivalent, it is not an equivalenty 
implementation (complexity). `system.arraycopy` uses memory operations to provide a constant time clone of the array. Python's 
implmentation is linear complexity

The end result was to implement a doubly linked list in code.
