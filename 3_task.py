# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 02:52:30 2022

@author: KENT
"""

#chislo = int(input("Введите число: "))                          #Вводим число для сравнения
#with open ("complex.txt","r") as f:     
  #  line = [line for line in f if abs(complex(line)) >= chislo] #Создаем генератор списка
   # for i in line:                                              #Создаем цикл для вывода наших чисел
   #    print("Больше или равно переменной chislo",i)            #Вывод переменной i           


chislo = float(input('Enter number'))
with open("complex.txt","r") as f:
    for line in f:
        if abs(complex(line))>=chislo:
            A = line
            print('mod >>>>>>',(A))
        else:
           B = line
           print('mod <<<<<<<',(B))
