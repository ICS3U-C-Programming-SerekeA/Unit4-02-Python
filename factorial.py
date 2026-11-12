#!/usr/bin/env python3
# Created by: Sereke Asfeday
# Created on: 10, November, 2026
# This program asks user for whole numbers and then
#  calculates the factorial of that number.


def main():
    # Initialize the variables
    loop_counter = 0
    factorial_answer = 1

    # Get the user number
    user_number_as_string = input("Enter a whole number: ")

    try:
        user_number = int(user_number_as_string)

        if user_number < 0:
            print("{} is not a positive whole number.".format(user_number))

        else:
            print("")

            # Replicates a do-while loop
            while True:
                loop_counter = loop_counter + 1
                factorial_answer = factorial_answer * loop_counter

                print("Tracking {} times through loop.".format(loop_counter))

                if loop_counter >= user_number:
                    break

            print("{}! = {}".format(user_number, factorial_answer))

    except ValueError:
        print("{} is not a valid whole number.".format(user_number_as_string))

    finally:
        print("")
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
