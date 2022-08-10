# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 10:35:57 2022

@author: yamchips
"""

import string

# a = 'purple#$%^cow'

# for i in string.punctuation:
#     if i in a:
#         a = a.replace(i, ' ')
# resList = a.split()
        
# res = [1,2,3,5,6]
# res == list(range(res[0],res[-1]+1))

# title = 'The pURple cow is soft and cuddly.'
# # phrase = 'puRPle cOW'
# phrase = input('Enter the phrase:').lower()

# def is_phrase_in(title, phrase):
#     def stringCollate(text):
#         '''
#         Input: string
#         Returns: a list, delete punctuations and spaces in the string
#         '''
#         for i in string.punctuation:
#             if i in text:
#                 text = text.replace(i, ' ')
#         return text.split()
    
#     title = title.lower()
    
#     titleList = stringCollate(title)
#     phraseList = stringCollate(phrase)
#     res = []
#     for item in phraseList:
#         if item in titleList:
#             res.append(titleList.index(item))
#         else:
#             return False
#     return res == list(range(res[0],res[-1]+1,1))

# print(is_phrase_in(title, phrase))


# from ps5 import *
# from datetime import timedelta

# dt = timedelta(seconds=5)
# now = datetime(2016, 10, 12, 23, 59, 59)
# now = now.replace(tzinfo=pytz.timezone("EST"))

# ancient_time = datetime(1987, 10, 15)
# ancient_time = ancient_time.replace(tzinfo=pytz.timezone("EST"))
# ancient = NewsStory('', '', '', '', ancient_time)

# just_now = NewsStory('', '', '', '', now - dt)
# in_a_bit = NewsStory('', '', '', '', now + dt)

# future_time = datetime(2087, 10, 15)
# future_time = future_time.replace(tzinfo=pytz.timezone("EST"))
# future = NewsStory('', '', '', '', future_time)

# timeStr = '12 Oct 2016 23:59:59'
# format_data = "%d %b %Y %H:%M:%S"
# date = datetime.strptime(timeStr, format_data).replace(tzinfo=pytz.timezone("EST"))

var = "t1"
varName = 'var'
s= locals()[varName]
s

s2=vars()[varName]
s2

s3=eval(varName)
s3






