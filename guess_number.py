from random import randint

number = randint(1, 100)
print('Угадайте число от 1 до 100')

while True:
    guess = int(input('Введите число: '))
    if guess < number:
        print('Выше число меньше загаданного')
    elif guess > number:
        print('Ваше число больше загаданного')
    elif guess == number:
        break

print('Вы угадали число')