#-*- coding: utf-8 -*-

"""
Created on Mon May 22 21:10:30 2023
author @ bjsiv

Main Application Backbone
PCPartProctor

"""

from datetime import *
from subMenuManager import directionalControl


def printTitle():

    pass


def printMenu():

    while True:

        try:
            printTitle()
            option = int(input('\tMenu option: '))
        except ValueError:
            print('\tNot a valid option. Please try again.')
            continue
        
        if option != 10 & option < 10:
            directionalControl(option)
        elif option != 10 & option > 10:
            print('\tInvalid input. Please choose an entry on the menu.')
        else:
            print('\tThank you for choosing PCPartProctor. Have a good day.')
            exit()

def signUserIn():

    print('#==============================================================#')
    print(
        '\tHello! Thank you for choosing PCPartProctor.'
    )
    today = date.today()
    print(f'\tCURRENT DATE: {today}')

    success = False
    while True:

        try:
            usr = str(input('\tPlease enter your username: '))
            paswd = str(input('\tPlease enter your password: '))
        except ValueError:
            print('\tInvalid input detected. Please try again.')
            continue

        # if user / pass match database then approve sign in.
        # if no match then request again. 
        # max of three wrong input before system shuts down for 15 minutes.
        # account lockout doubles every time window is missed. 
        # account lockout reset after every 45 minutes. 

        if success == True:
            return 0
            break
        elif success == False:
            return 1
            break
        else:
            print('\tAn error has occured. Please try again.')
            continue


def main():

    signUserIn()
    direction = printMenu()
    directionalControl(direction)


if __name__ == "__main__":
    main()