#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    
    my_sequence = [0, 1]
    while len(my_sequence) < length:
        my_sequence.append(my_sequence[-1] + my_sequence[-2])
    
    print(my_sequence[:length])