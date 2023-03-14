# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 11:37:28 2023

@author: Oliver
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list_out = []
    for i in range(x+1):
        print("i: ", i)
        for j in range(y+1):
            print("j: ", j)
            for k in range(z+1):
                print("k: ", k)
                print("Sum: ", i+j+k)
                if i + j + k != n:
                    print(i,j,k)
                    list_out.append([i,j,k])
    print(list_out)
    
    # Using list comprehension instead of loops    
    ls = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(ls)