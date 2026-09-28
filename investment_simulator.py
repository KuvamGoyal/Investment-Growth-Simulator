#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:59:15 2026

Description: This project can be used to address the following question: If I
             invest $X every month for Y years at Z% annual returns, what will
             be the future and present value of this investment project. 

@author: kuvamgoyal
"""

cash_flows = float(input('Input how much money will be invested every month: '))
principal = float(input('How much is the principal amount invested? '))
years = float(input('How many years will payments last? '))
rate = float(input('What is the effective annual interest rate? ')) * 0.01
monthly_rate = rate/12

def present_value(cash_flows, principal, years, monthly_rate):
    pv = principal + cash_flows * (1 - (1 + monthly_rate)**(-years * 12))/monthly_rate
    return pv

def future_value(cash_flows, principal, years, monthly_rate):
    fv = principal * (1 + rate) ** years + cash_flows * ((1 + monthly_rate)**(years * 12) - 1)/monthly_rate
    return fv

pv = present_value(cash_flows, principal, years, monthly_rate)
fv = future_value(cash_flows, principal, years, monthly_rate)

print('The present value of the investments is', pv)
print('The future value of the investments is', fv)

# Now make it so that it plots what the total investment will look like over time. 
  
time = list(range(0, int(years)+1))
yearly_balances = []

for year in time:
    balance = future_value(cash_flows, principal, year, monthly_rate)
    yearly_balances.append(balance)
    
import matplotlib.pyplot as plt

fig1 = plt.figure()         
plt.plot(time,yearly_balances)
plt.xlabel('Time (years)')    
plt.ylabel('Value ($)')       
plt.title('Value of investment every year')
plt.grid()                    
plt.show()                    

