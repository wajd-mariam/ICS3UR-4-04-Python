# !/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: Novemeber 2019
# This is a number guessing program using while loop

import random


def main():

    random_number = random.randint(1, 5)

    # loop & input & process & output
    # while loop
    while True:
        try:
            number = int(input("Can you guess a number from 0-5? "))

            if (number == random_number):
                print("You guessed it!")
                break
            else:
                print("Sorry, you couldn't guess it")
        except Exception:
            print("Invalid entry")
            break
        finally:
            print("Thanks for using my program")


if __name__ == "__main__":
    main()
