#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:10:53 2022

@author: lucianavarromartin
"""

from multiprocessing import Process
from multiprocessing import current_process 
from multiprocessing import Value, Array


N= 8
#common,turn variable común, representa la memoria compartida
def task(common, tid, turn):
    a= 0 #variable local, cada proceso tiene su copia de a y es
         # independiente
    for i in range(100):
        print(f'{tid}−{i}: Non−critical Section')
        a += 1
        print(f'{tid}−{i}: End of non−critical Section') 
        while turn.value!=tid:
            pass
        print(f'{tid}−{i}: Critical section')
        v = common.value + 1 
        print(f'{tid}−{i}: Inside critical section') 
        common.value = v
        print(f'{tid}−{i}: End of critical section') 
        turn.value = (tid + 1) % N
        
def main(): 
    lp = []
    common = Value('i', 0) 
    turn = Value('i', 0) 
    for tid in range(N):
        lp.append(Process(target=task, args=(common, tid, turn)))
        #todos los procesos son independientes
        #p.start() los procesos se ejecutan todos 
    print (f"Valor inicial del contador {common.value}")
    for p in lp:
        p.start()
        
    for p in lp: 
        p.join()
        
    print (f"Valor final del contador {common.value}") 
    print ("fin")
    
if __name__ == "__main__": 
    main()