#-*- coding: utf-8 -*-

"""
Created on Tue May 23 06:30:40 2023
author @ bjsiv

Sub-Menu Management
PCPartProctor

"""

from accountManager import *

def userAuthenticationCenter():
    
    while True:

        option = str(input('\tYou have chosen the User Account Center. Please choose one of the following options.'))

        try:
            print("Please choose one of the following options:")
        except ValueError:
            print('\tInvalid input. Please try again.')
            continue

        if input == 1:
            user.createNewUser()
        elif input == 2:
            user.signUserIn()
        elif input == 3:
            print('\tThank you for choosing PCPartProctor. Have a good day.')

def partsDatabase():
    pass


def personalPartList():
    pass


def personalBuildList():
    pass


def compatibilityCheck():
    pass


def checkPartPres():
    pass


def addPartDB():
    pass


def remPartDB():
    pass


def signOut():
    pass

def directionalControl(direction):

    while True:

        if direction == 1:
            userAuthenticationCenter()
        elif direction == 2:
            pass
        elif direction == 3:
            pass
        elif direction == 4:
            pass
        elif direction == 5:
            pass
        elif direction == 6:
            pass
        elif direction == 7:
            pass
        elif direction == 8:
            pass
        elif direction == 9:
            pass
        else:
            print('\tAn error has occured. Please try again.')