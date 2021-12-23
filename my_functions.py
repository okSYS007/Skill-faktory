const_Pi = 3.14

def get_circle(r):
    return const_Pi*r*r

def get_square(a, b):
    return a * b

if __name__ == '__main__':
   # проверяем работоспособность функции, дальнейшая часть не будет импортирована
   assert get_circle(5) == 78.5  # если ответы будут отличаться, то будет вызвана ошибка
   assert get_square(5, 4) == 20