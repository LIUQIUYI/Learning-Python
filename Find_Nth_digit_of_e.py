# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:28:13 2018

@author: lqy45
"""


def get_approximate_euler(n=1000):
    """input a int number n in this function, the output is an int number
    of e with accurancy to n decimal places, For example, input n=10,the out put 
    is 271828182840(including 12 numbers), add a point to the out put is 
    2.71828182840, the last number 0, is inaccurate. 
    """
    import time
    time_start=time.time()
    one=10**(n+1)
    a_k=one
    a_sum=one
    k=1
    while 1:
        a_k//=k
        if a_k<1:
            break
        a_sum+=a_k
        k+=1
    euler=a_sum
    time_end=time.time()
    print('time cost'+':'+str(time_end-time_start)+'s')
    return euler
x=str(get_approximate_euler(200000))
file = open('test_e.txt','w')
for i in x:
    file.write(i)
file.close()
        
