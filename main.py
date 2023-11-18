import os
import time
import random

while True:
    os.system('cls')

    choice = ['Rock', 'Paper', 'Scissors']

    win_msg = "You win!"

    draw_msg = "Draw!"

    bot_win_msg = "Bot wins!"

    for a in choice:
        print(str((choice.index(a)+1)) + ": " + a)

    try:
        player_choice = choice[int(input())-1]
    except ValueError:
        print("Invalid choice!")
        time.sleep(3)
        continue

    except IndexError:
        print("Invalid choice!")
        time.sleep(3)
        continue

    bot_choice = choice[random.randint(0, 2)]
    print("Bot's Choice is: ", bot_choice)
    print("Your Choice is: ", player_choice)

    if player_choice == bot_choice:
        print(draw_msg)
        time.sleep(3)
        continue

    elif (player_choice == 'Rock') and (bot_choice == 'Scissors'):
        print(win_msg)
        time.sleep(3)
        continue

    elif (player_choice == 'Paper') and (bot_choice == 'Rock'):
        print(win_msg)
        time.sleep(3)
        continue

    elif (player_choice == "Scissors") and (bot_choice == 'Paper'):
        print(win_msg)
        time.sleep(3)
        continue

    else:
        print(bot_win_msg)
        time.sleep(3)
        continue