# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 11:44:57 2023

@author: Oliver
"""
#import numpy as np
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort(reverse=True)
    print(arr)
    max_score = arr[0]
    runner_up = 0
    for i in range(n):
        if arr[i] < max_score and arr[i] > runner_up:
            runner_up = arr[i]
    print(runner_up)