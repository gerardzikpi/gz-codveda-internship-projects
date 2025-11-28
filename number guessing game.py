import random


secret_number=random.randint(1,50)


while True:
    user_input = int(input('Guess the number: '))

    # def validate_input():
    #     try:
    #         if user_input is not int():
    #             pass
    #     except ValueError:
    #         raise ValueError("Input must be an integer")


    def playing():
        if user_input==secret_number:
            print('Congratulations, You won')
            if user_input > 50:
                print("The number is not within the range of the secret number")

        elif user_input < secret_number:
            print("Guess too low")
            print(f"the correct number is:{secret_number}")

            if user_input > 50:
                print("The number is not within the range of the secret number")

        elif user_input > secret_number:
            print("Guess too high")
            print(f"the correct number is: {secret_number}")

            if user_input > 50:
                print("The number is not within the range of the secret number")

        else:
            print("please enter a valid input")

    playing()

    continue_playing = input("Continue playing(y/n): ")
    if continue_playing == 'y':
        continue
    playing()
    if continue_playing == 'n':
        break
    else:
        print("Input is not among choices. enter an input from the above choices.")