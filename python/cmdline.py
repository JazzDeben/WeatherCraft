## Dear reader
## Thanks for your interest in this software
## This software is free to use and modify
## There is currently no licence attached to this software
## I assume no responsibility with regards to the utilisation of this software
## No creepers, or any other mobs, were hurt during the realisation or utilisation of this software
##
## Géry Ducatel
##

import sys          # used to capture user input
import re           # regular expression
import logging      # a logger library

from telnetapi import rain, sun, toggleweather, day, night

def launch(user, password, targetip, portnumber):

    logger = logging.getLogger('wc.controller')
    logger.info('Starting cmdline python file')

    while True:
        print("If you want to exit type 0")
        print("If you want rain type 1")
        print("If you want sun type 2")
        print("If you want day type 3")
        print("If you want night type 4")
        choice = input("Enter your choice: ")

        if choice == '0':
            print("Your choice is " + choice)
            break
        
        nreg = re.compile(r"^\d{1}$")
        nmatch = nreg.match(choice)

        if not nmatch:
            logger.debug('Test module - invalid entry (has to be a single digit) ')
            print("This is not a valid choice")
            continue

        if choice == '1':
            logger.debug('Test module - choice 1')
            print("Your choice is " + choice)
            rain(user, password, targetip, portnumber)
            continue

        if choice == '2':
            logger.debug('Test module - choice 2')
            print("Your choice is " + choice)
            sun(user, password, targetip, portnumber)
            continue

        if choice == '3':
            logger.debug('Test module - choice 3')
            print("Your choice is " + choice)
            day(user, password, targetip, portnumber)
            continue

        if choice == '4':
            logger.debug('Test module - choice 4')
            print("Your choice is " + choice)
            night(user, password, targetip, portnumber)
            continue

        else:
            continue

        break;

    
