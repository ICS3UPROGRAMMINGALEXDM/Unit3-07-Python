#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: Program that decides if the user can date or not
import colorama
from colorama import Fore, Style


def main():
    # loop allows the user to re-enter if input was initially invalid
    while True:
        # get user input
        rich = input(Fore.WHITE + "Are you rich? (y/n): ")
        g_looks = input("Are you good looking? (y/n): ")

        # Checks to make sure input is valid
        if (g_looks == "y" or g_looks == "n") and (rich == "y" or rich == "n"):
            # Decides what to display with given inputs
            if g_looks == "y" or rich == "y":
                print(
                    Fore.GREEN
                    + Style.BRIGHT
                    + "Congratulations, You can date our grandchild!"
                )
                break
            else:
                print(
                    Fore.YELLOW
                    + Style.BRIGHT
                    + "Imagine not being rich or good looking lol. Sorry bud."
                )
                break
        else:
            print(Style.BRIGHT + Fore.RED + "Invalid Input. Try again please")


if __name__ == "__main__":
    main()
