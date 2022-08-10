# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 15:57:44 2022

@author: yamchips
"""

'''User input, including the total cost of dream house, annual salary
   and the portion saved'''
total_cost = float(input('Enter the cost of your dream house: '))
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))

'''Invariant setting'''
portion_down_payment = 0.25
r = 0.04

'''Compare the saving and the cost of dream house, use month to
   calculate time'''
current_savings = 0
month = 0
while current_savings <= total_cost * portion_down_payment:
    current_savings += annual_salary*portion_saved/12 \
        + current_savings*r/12 
    month += 1

print('Number of months: ', month)