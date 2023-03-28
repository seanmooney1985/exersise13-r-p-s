import random


def get_choice(user_input):
    if user_input == 'R':
        return 'Rock'
    elif user_input == 'P':
        return 'Paper'
    elif user_input == 'S':
        return 'Scissors'
    else:
        return None


def play_game():
    user_input = input("Enter R for Rock, P for Paper, or S for Scissors: ").upper()
    user_choice = get_choice(user_input)

    while user_choice is None:
        user_input = input("Invalid choice. Please enter R, P, or S: ").upper()
        user_choice = get_choice(user_input)

    computer_choice = random.randint(0, 2)

    if computer_choice == 0:
        computer_choice = 'Rock'
    elif computer_choice == 1:
        computer_choice = 'Paper'
    else:
        computer_choice = 'Scissors'

    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.\n")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'Rock' and computer_choice == 'Scissors':
        print("You win!")
    elif user_choice == 'Paper' and computer_choice == 'Rock':
        print("You win!")
    elif user_choice == 'Scissors' and computer_choice == 'Paper':
        print("You win!")
    else:
        print("You lose!")


play_game()
