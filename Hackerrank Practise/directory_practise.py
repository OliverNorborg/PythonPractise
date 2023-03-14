# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:06:22 2023

@author: Oliver
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    #student_marks = list(student_marks)
    query_name = input()
    query_scores = student_marks.get(query_name)
    avg_score = sum(query_scores)/len(query_scores)
    print("%.2f" % avg_score)
    