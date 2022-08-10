# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 21:36:49 2022

@author: yamchips
"""

'''
Three ways to find the key 
'''

exampleDict = {'a':'e', 'e':'i', 'i':'o', 'o':'u', 'u':'a'}

#Method 1: using list
listkey = list(exampleDict.keys())
listval = list(exampleDict.values())
num = listval.index('o')

#in 1 line:
list(exampleDict.keys()) [list (exampleDict.values()).index ('o')]

print(listkey[num])

#Method 2: defining a function
def get_key (dict, value):
    for k, v in dict.items():
        if v == value:
            return k 

print(get_key(exampleDict, 'o'))

#Method 3: reversing keys and values in the original dict
new_dict = {v : k for k, v in exampleDict.items()}
print(new_dict['o'])