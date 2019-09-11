#GuessGame
import tkinter as tk #библиотека для gui
import random #подключаем библиотеку для генерации псевдо-случайных чисел
#from msvcrt import getch - пока не разобрался
guessCount = 1
#количество попыток случайно от 1 до 5
guessLimit = random.randrange(1, 6)
#ответ на вопрос будет генерироваться случайным образом каждую игру. Ответом будет число от 1 до 15.
secretNumber = random.randrange(1, 16)

#формируем gui
window = tk.Tk()
window.title("Guess or take dick in the face")
window.geometry("640x480")

#LABEL
title = tk.Label(text=)
window.mainloop()

#функция для защиты от ебланов, проверка на то, что введено целое число
def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print("Готов ли ты испытать свою удачу в этой опасной игре с цифрами и хуями? Нажми Д и enter, если готов")
askOfReadiness = input().upper()
if askOfReadiness == "Д" or askOfReadiness == "L":
    print("Вперёд же, бесстрашный герой! Угадывай число от 1 до 15 включительно.")
else:
    exit("Не место тебе здесь, ссыкло")
if guessLimit == 1:
    print("У тебя всего 1 попытка")
elif guessLimit == 5:
    print("У тебя целых 5 попыток, попытайся их не просрать, мудень")
else:
    print("У тебя " + str(guessLimit) + " попытки")

while guessCount <= guessLimit:
    guess = input("Попытка №" + str(guessCount) + ": ")
    #проверяем введена ли именно цифра, а не какой-то другой символ
    if isint(guess):
        if int(guess) == secretNumber:
            print("Угадал! Вот тебе большой и сочный 8====Э")
            break  # прерываем цикл при победе
        if 0 < int(guess) < 16:
            print("Не угадал")
            guessCount += 1
        else:
            print("Читать не умеешь или что? Введи число от 1 до 15")
    else:
        print("Вводи число")
else:
    print("Ты потерпел сокрушительное поражение, проверяя свою удачу. Это было число " + str(secretNumber))
