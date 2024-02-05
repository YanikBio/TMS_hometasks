'''
Следует добавить возможность выбирать количество шагов, это можно реализовать с помощью 
вычисления длины и если это превышает длину строки алфовита, просто прибавлять остаток к 0
Также, следует добавить возможность добавления распознавания определённых знаков, как минимум, 
знаков пунктуации
'''

def criptoCeaser(message, alphabet: str, rot=1):  # шифрую 
    cripto_message = ''
    for letter in message:
        if letter == ' ':
            cripto_message += '_'
            continue
        i = alphabet.find(letter)
        cripto_message += alphabet[rot+i]

    return cripto_message

def decriptoCeaser(cripto_messege, alphabet, rot=-1):  # расшифровываю
    message = ''
    for letter in cripto_messege:
        if letter == ' ':
            message += '_'
            continue
        i = alphabet.find(letter)
        message += alphabet[rot+i]
    
    return message

ru_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'

l = input('Выберете язык: r - русский, e - английский ')
s = input('Выберете режим: s - шифровка, d - дешифровка ')

message = input('Введите сообщение: ')

if l == 'r':
    if s == 's':
        print(criptoCeaser(message, ru_alphabet))
    elif s == 'd':
       print(decriptoCeaser(message, ru_alphabet))
elif l == 'e':
    if s == 's':
        print(criptoCeaser(message, eng_alphabet))
    elif s == 'd':
        print(decriptoCeaser(message, eng_alphabet))

