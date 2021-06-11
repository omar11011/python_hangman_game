import os
import random

def getWord():
    with open('words.txt', 'r', encoding="utf-8") as f:
        count = 0
        keys = list(f)

        # Eliminando el caracter "\n" de cada palabra
        for i in keys:
            array = list(i)
            if array[len(array) - 1] == '\n': character_removed = array.pop(len(array) - 1)
            keys[count] = ''.join(array)
            count += 1

        return random.choice(keys).upper()

def run():
    win = False
    attempts = 5
    word = getWord()
    lines = ['_ '] * len(word)
    
    # Juego
    while attempts > 0:
        os.system('cls')

        print(''.join(lines))
        print('\nIntentos: ' + str(attempts) + '\n')

        if '_ ' in lines:
            option = input('Introduce una letra o adivina la palabra: ')

            if option == '': continue
            else: option = option.upper()

            # Usuario inserta un caracter
            if len(option) == 1:
                if(option in list(word)):
                    if option + ' ' in lines: continue

                    position = 0
                    for i in list(word):
                        if i == option: lines[position] = option + ' '
                        position += 1
                else: attempts -= 1
            # Usuario inserta la palabra posible
            else:
                if option == word:
                    win = True
                    attempts = 0
                else: attempts -= 1
        else:
            win = True
            attempts = 0

    os.system('cls')
    position = 0

    # Mostrando la palabra final
    for i in lines:
        if i == '_ ':
            lines[position] = list(word)[position] + ' '
        position += 1
    print(''.join(lines))
    
    if win == False:
        return print('¡Has perdido! 😪')
    else:
        return print('¡Felicidades, has ganado! 🤑')

if __name__ == '__main__':
    run()