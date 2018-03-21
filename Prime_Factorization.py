# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:01:15 2018

@author: lqy45
"""

def find_factorization(n):
    """function to find out all the factorizations of n , except 1 and n itself"""
    list1=[]
    for i in range(1,n//2+1):
        if n%i==0:
            list1.append(int(i))
    list2=[]
    for item in list1:
        list2.append(int(n/item))
    factorization_list=set(list1+list2)
    factorization_list.remove(1)
    factorization_list.remove(n)
    if len(factorization_list):
        return factorization_list
    else:
        print("the factorization is " + str(n) + " itself")
        return n
    
def find_prime_factorization(n):
    """find all the prime factorization of n, time depend on the biggest prime
    factorization. For example,12394992930 cost 16.72s to get [2, 3, 5, 413166431] """
    import time
    time_start=time.time()
    list1=help_finding_prime_factorizations(n)
    confirmed=[]
    if list1==n:
        print("itself")
    else:
        a=min(list1)
        b=max(list1)
        confirmed=[a]
        while b!=n:
            list_update=help_finding_prime_factorizations(b)
            if list_update!=b:
                a=min(list_update)
                confirmed.append(a)
                b=max(list_update)
            else:
                confirmed.append(b)
                break
            
    time_end=time.time()
    print('time cost'+':'+str(time_end-time_start)+'s')
    return confirmed
            
def help_finding_prime_factorizations(n):
    """funciton fing_factorization() is used to find all the factorizations 
    except itself and 1, this function is helpful to accelerate the process of 
    find_prime_factorization()"""
    basic_factorization_list=[]
    #在函数里的变量需要声明
    for i in range(2,n//2+1):
        if n%i==0:
            basic_factorization_list.append(i)
            basic_factorization_list.append(int(n/i))
            break
    if len(basic_factorization_list):
        return basic_factorization_list
    else:
        return n
            
        
    
            
        
    
    
        
    