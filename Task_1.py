import random

def guessing_game():
    answer = random.randint(1,10)
    while True:
        try:
            user_guess = int(input('Каковы ваши предположения ? '))
            if user_guess == answer:
                print(f'Правильно! Ответ {user_guess}')
                break
            if user_guess < answer:
                print(f'Ваше число {user_guess} слишком маленькое!')
            if user_guess > answer:
                print(f'Ваше число {user_guess} слишком большое!')
        except ValueError:
            print("Введите числавое выражение !")
            
guessing_game()