#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:16:46 2022

@author: lucianavarromartin
"""

from multiprocessing import Process
from multiprocessing import current_process 
from multiprocessing import Value, Array


N= 8
def is_anybody_inside(critical, tid):
    found = False
    i= 0
    while i<len(critical) and not found:
        found = tid!=i and critical[i]==1
        i += 1
    return found

def task(common, tid, critical):
    a= 0
    for i in range(100):
        print(f'{tid}−{i}: Non−critical Section')
        a += 1
        print(f'{tid}−{i}: End of non−critical Section') 
        while is_anybody_inside(critical, tid):
            pass
        critical[tid] = 1 
        print(f'{tid}−{i}: Critical section')
        v = common.value + 1 
        print(f'{tid}−{i}: Inside critical section') 
        common.value = v
        print(f'{tid}−{i}: End of critical section') 
        critical[tid] = 0
        
def main():
    lp = []
    common = Value('i', 0) 
    critical = Array('i', [0]*N) 
    for tid in range(N):
        lp.append(Process(target=task, args=(common, tid, critical))) 
        print (f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()
    
    for p in lp: 
        p.join()
    # si el valor común no es 800 y es por ej 753, es que ha habido
    # problemas de concurrencia
    # ejemplo que vimos en clase que no respeta la exclusión mutua
    print (f"Valor final del contador {common.value}") 
    print ("fin")

if __name__ == "__main__":
    main()
