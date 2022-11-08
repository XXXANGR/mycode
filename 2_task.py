spisok = {'A':[],'B':[],'C':[],'D':[],'E':[]}   #Создаем словарь
spisok['A'] = float(input('value A:'))          #Вводим значение ключей
spisok['B'] = float(input('value B:'))          #Вводим значение ключей
spisok['C'] = float(input('value C:'))          #Вводим значение ключей
spisok['D'] = float(input('value D:'))          #Вводим значение ключей
spisok['E'] = float(input('value E:'))          #Вводим значение ключей
print(spisok)

#spisok = {'A':[],'B':[],'C':[],'D':[],'E':[]}
#spisok[0] = input('value A')
#spisok[1] = input('value B')
#spisok[2] = input('value C')
#spisok[3] = input('value D')
#spisok[4] = input('value E')
#print(spisok)

#spisok = {'A':[],'B':[],'C':[],'D':[],'E':[]}
#A = float(input('value A:'))
#B = float(input('value B:'))
#C = float(input('value C:'))
#D = float(input('value D:'))
#E = float(input('value E:'))
#dict_sample = spisok.fromkeys(spisok, A,B,C,D,E) 
#print(dict_sample)

f = open('slovar.txt','w')                     #Создаем файл для записи данных
f.write(str(spisok))                           #Записывем Словарь в строку
f.close()                                      #Закрываем файл
