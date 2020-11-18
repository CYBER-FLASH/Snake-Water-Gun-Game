import random
first_random = ['s','w','g']
chance = 5
no_of_chance = 0
humun_point = 0
computer_point = 0

start_game = print("1 - Start Game")
_read = print("2 - Read Terms And Conditions On Game")
enter_choice = int(input("Enter Choice Here : \n"))

if enter_choice == 1:
    print("s for snake\nw for water\ng for gun")

    while no_of_chance < chance:
        _input = input('snake,water,gun :')
        _random = random.choice(first_random)

        if _input == "s" and _random == "g":
            computer_point = computer_point + 1
            print(f"your guess {_input} and computer point guess {_random}\n")
            print("computer wins 1 point")
            print(f"humun point is {humun_point} and computer point is {computer_point}")

        elif _input == "s" and _random == "w":
            humun_point = humun_point + 1
            print(f"your guess {_input} and computer point guess {_random}\n")
            print("humun wins 1 point")
            print(f"humun point is {humun_point} and computer point is {computer_point}")

        elif _input == "w" and _random == "s":
            computer_point = computer_point + 1
            print(f"your guess {_input} and computer point guess {_random}\n")
            print("computer wins 1 point")
            print(f"humun point is {humun_point} and computer point is {computer_point}")

        elif _input == "w" and _random == "g":
            humun_point = humun_point + 1
            print(f"your guess {_input} and computer point guess {_random}\n")
            print("computer wins 1 point")
            print(f"humun point is {humun_point} and computer point is {computer_point}")

        elif _input == "g" and _random == "s":
            humun_point = humun_point + 1
            print(f"your guess {_input} and computer point guess {_random}\n")
            print("humun wins 1 point")
            print(f"humun point is {humun_point} and computer point is {computer_point}")

        elif _input == "g" and _random == "w":
            computer_point = computer_point + 1
            print(f"your guess {_input} and computer point guess {_random}\n")
            print("humun wins 1 point")
            print(f"humun point is {humun_point} and computer point is {computer_point}")
        else:
            print("you have wrong input")
        no_of_chance = no_of_chance + 1
        print(f"{chance - no_of_chance} is left out of {chance}\n")

    if computer_point == humun_point:
        print("Tie")
    elif computer_point > humun_point:
        print("Computer Win And You Loose")
    else:
        print("You Win And Computer Loose")

    print(f"your point is {humun_point} and computer point is {computer_point}")


else:
    print("(1) - you have Only 5 chance in this game\n")
    print("(2) - S - Snake\n\tW - Water\n\tG - Gun\n")
















