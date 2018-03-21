# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:46:08 2018

@author: lqy45
"""

def creating_fibonacci_sequence(longth=1000):
    Fib1=0
    Fib2=1
    Fib_list=[0,1]
    k=2
    while 1:
        Fib=Fib2
        Fib2=Fib2+Fib1
        Fib1=Fib
        Fib_list.append(Fib2)
        k+=1
        if k>longth:
            break
    return Fib_list
        
def find_number_in_fibonacci(n,m):
    if n in creating_fibonacci_sequence(m):
        return "ture"
    else:
        return "None"