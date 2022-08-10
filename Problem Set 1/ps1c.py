# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 16:52:05 2022

@author: yamchips
"""
# import random

'''User input: starting annual salary'''
annual_salary = float(input('Enter the starting salary: '))

'''Invariant setting'''
portion_down_payment = 0.25
r = 0.04
semi_annual_raise = .07
total_cost = 1000000
down_payment = total_cost * portion_down_payment

def savingcal(salary, rate):
    '''
    Parameters
    ----------
    salary : float
        annual salary, increase every 6 months
    rate : float, (0,1)
        saving rate

    Returns
    -------
    savings : float
        total savings after 3 years.

    '''
    savings = 0
    for month in range(1,37):
        savings += salary*rate/12 + savings*r/12 
        if month%6 == 0:
            salary = salary * (1 + semi_annual_raise)
    return savings

'''Compare savings and down payment, using step to record search steps
   set initial rate to 0.5'''
if savingcal(annual_salary, 1) < down_payment:
    print('It is not possible to pay down payment in three years')
else:
    # rate = round(random.uniform(0, 1),4)
    rate = 0.5
    step = 0
    low = 0.0001
    high = 0.9999
    flag = False
    while not flag:
        if savingcal(annual_salary, rate)-down_payment > 100:
            high = rate
            rate = (low + rate)/2
            rate = int(rate*10000)/10000 #two decimals of accuracy
            step += 1
        elif savingcal(annual_salary, rate)-down_payment < -100:
            low = rate
            rate = (rate + high)/2
            rate = int(rate*10000)/10000
            step += 1
        if abs(savingcal(annual_salary, rate)-down_payment) < 100:
            flag = True
            step += 1
    print('Best saving rate:', rate)
    print('Steps in bisection search:', step)




