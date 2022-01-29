#Напишите программу, которая отправляет запрос на генерацию случайных текстов 
#Выведите первый из сгенерированных текстов.

import requests
import json # импортируем необходимую библиотеку
 
 
r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
texts = json.loads(r.content) # делаем из полученных байтов python объект для удобной работы

print(texts[0])
print('')
for i in texts:
    print(i)