import random
def guessing_game():
    answer = random.randint(1,10)
    count = 3
    while count:
        try:
            print(f'Игра началось, у вас {count} попытки \n')
            user_guess = int(input('Каковы ваши предположения ?'))
            if user_guess == answer:
                print(f'Правильно! Ответ {user_guess}')
                break
            if user_guess < answer:
                print(f'Ваше число {user_guess} слишком маленькое!')
                count -= 1
            if user_guess > answer:
                print(f'Ваше число {user_guess} слишком большое!')
                count -= 1
        except ValueError:
            print("Введrdrте числавое выражение !")
    print('Вы не отгадали число !')
            
guessing_game()