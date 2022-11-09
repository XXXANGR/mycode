spisok = {'A':[],'B':[],'C':[],'D':[],'E':[]}   #Создаем словарь
spisok['A'] = float(input('value A:'))          #Вводим значение ключей
spisok['B'] = float(input('value B:'))          #Вводим значение ключей
spisok['C'] = float(input('value C:'))          #Вводим значение ключей
spisok['D'] = float(input('value D:'))          #Вводим значение ключей
spisok['E'] = float(input('value E:'))          #Вводим значение ключей
print(spisok)
f = open('slovar.txt','w')                     #Создаем файл для записи данных
f.write(str(spisok))                           #Записывем Словарь в строку
f.close()                                      #Закрываем файл
