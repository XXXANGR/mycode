# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 20:12:04 2022

@author: KENT
"""
import time  
import math 
import cmath
N = float(input("Please enter number: "))    #Вводится число
print('math\n','-----------------')          #Шапка таблицы    
st_sin = time.time()                         #Начало отсчета старта программы для sin
for i in range(1000000):                    
    out = math.sin(N)                        #Вычисление синуса числа N
print('|sin | %f5 |' % (time.time()-st_sin)) #Вывод строки и время выполнение на экран
print('-----------------')
st_log = time.time()                         #Начало отсчета старта программы для log
for i in range(1000000):
    out1 = math.log(N)                       #Вычисление логарифма числа N
print('|log | %f5 |' % (time.time()-st_log)) #Вывод строки и время выполнение на экран
print('-----------------')
st_sqrt = time.time()                        #Начало отсчета старта программы для sqrt
for i in range(1000000):
    out2 = math.sqrt(N)                      #Вычисление квадратного корня числа N
print('|sqrt| %f5 |' % (time.time()-st_sqrt))#Вывод строки и время выполнение на экран
print('-----------------')                   #Конец таблицы                  

#То же самое но для библиотеки cmath
print('cmath\n','-----------------')
st_sin = time.time()
for i in range(1000000):
    out = cmath.sin(N)
print('|sin | %f5 |' % (time.time()-st_sin))
print('-----------------')
st_log = time.time()
for i in range(1000000):
    out1 = cmath.log(N)
print('|log | %f5 |' % (time.time()-st_log))
print('-----------------')
st_sqrt = time.time()
for i in range(1000000):
    out2 = cmath.sqrt(N)
print('|sqrt| %f5 |' % (time.time()-st_sqrt))
print('-----------------')


    
    
