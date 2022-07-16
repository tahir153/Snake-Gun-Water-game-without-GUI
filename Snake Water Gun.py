# Snake Water Gun game
import random

lst = ['s', 'w', 'g']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print('\t\tSnake Water Gun\n')
print('Press w for water')
print('Press s for snake')
print('Press g for gun')

while no_of_chance < chance:
    _input = input('Snake,Water,Gun:')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie Both 0 point to each \n ")

    elif _input == 's' and _random == 'g':
        computer_point = computer_point + 1
        print(f"Your guess was '{_input}' ,Computer guess was  '{_random}'\n")
        print("computer wins")
        print(f"your score'{human_point}', computer's score'{computer_point}'\n")

    elif _input == 's' and _random == 'w':
        human_point = human_point + 1
        print(f"Your guess was '{_input}' ,Computer guess was '{_random}'\n")
        print("you win")
        print(f"your score'{human_point}', computer's score'{computer_point}'\n")

    elif _input == 'g' and _random == 's':
        human_point = human_point + 1
        print(f"Your guess was' {_input}' ,Computer guess was '{_random}'\n")
        print("you win")
        print(f"your score'{human_point}', computer's score'{computer_point}'\n")

    elif _input == 'g' and _random == 'w':
        computer_point = computer_point + 1
        print(f"Your guess was '{_input}' ,Computer guess was '{_random}'\n")
        print('you win')
        print(f"your score'{human_point}', computer's score'{computer_point}'\n")

    elif _input == 'w' and _random == 's':
        computer_point = computer_point + 1
        print(f"Your guess was '{_input}' ,Computer guess was '{_random}'\n")
        print('computer wins')
        print(f"your score'{human_point}', computer's score'{computer_point}'\n")

    elif _input == 'w' and _random == 'g':
        human_point = human_point + 1
        print(f"Your guess was '{_input}' ,Computer guess was '{_random}'\n")
        print('you win')
        print(f"your score'{human_point}', computer's score'{computer_point}'\n")
    else:
        print('Please input correct option.\n')

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point == human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")
