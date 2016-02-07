## Dear reader
## Thanks for your interest in this software
## This software is free to use and modify
## There is currently no licence attached to this software
## I assume no responsibility with regards to the utilisation of this software
## No creepers, or any other mobs, were hurt during the realisation or utilisation of this software
##
## Gery Ducatel
##


import telnetlib    # the library to place telnet calls
import logging      # a logger library

def rain(user, password, targetip, portnumber):

    buser = bytearray()
    buser = user.encode('UTF-8')

    bpassword = bytearray()
    bpassword = password.encode('UTF-8')

    logger = logging.getLogger('wc.controller')
    logger.info('Starting rain function in telnetapi')
    logger.debug('calling telnet with following arguments: ' + user + ' ' + password + ' ' + targetip + ' ' + portnumber)

    tn = telnetlib.Telnet(targetip, portnumber)

    tn.write(buser + b"\n")
    tn.write(bpassword + b"\n")
    tn.write(b"\n")
    tn.write(b"weather rain\n")
    tn.close()

    logger.debug('closing telnet')
    return

def sun(user, password, targetip, portnumber):

    buser = bytearray()
    buser = user.encode('UTF-8')

    bpassword = bytearray()
    bpassword = password.encode('UTF-8')

    logger = logging.getLogger('wc.controller')
    logger.info('Starting sun function in telnetapi')
    logger.debug('calling telnet with following arguments: ' + user + ' ' + password + ' ' + targetip + ' ' + portnumber)

    tn = telnetlib.Telnet(targetip, portnumber)

    tn.write(buser + b"\n")
    tn.write(bpassword + b"\n")
    tn.write(b"\n")
    tn.write(b"weather clear\n")
    tn.close()

    logger.debug('closing telnet')
    return


def toggleweather(user, password, targetip, portnumber):

    buser = bytearray()
    buser = user.encode('UTF-8')

    bpassword = bytearray()
    bpassword = password.encode('UTF-8')

    logger = logging.getLogger('wc.controller')
    logger.info('Starting toggleweather function in telnetapi')
    logger.debug('calling telnet with following arguments: ' + user + ' ' + password + ' ' + targetip + ' ' + portnumber)

    tn = telnetlib.Telnet(targetip, portnumber)

    tn.write(buser + b"\n")
    tn.write(bpassword + b"\n")
    tn.write(b"\n")
    tn.write(b"toggledownfall\n")
    tn.close()

    logger.debug('closing telnet')
    return


def day(user, password, targetip, portnumber):

    buser = bytearray()
    buser = user.encode('UTF-8')

    bpassword = bytearray()
    bpassword = password.encode('UTF-8')

    logger = logging.getLogger('wc.controller')
    logger.info('Starting day function in telnetapi')
    logger.debug('calling telnet with following arguments: ' + user + ' ' + password + ' ' + targetip + ' ' + portnumber)

    tn = telnetlib.Telnet(targetip, portnumber)

    tn.write(buser + b"\n")
    tn.write(bpassword + b"\n")
    tn.write(b"\n")
    tn.write(b"time set day\n")
    tn.close()

    logger.debug('closing telnet')
    return


def night(user, password, targetip, portnumber):

    buser = bytearray()
    buser = user.encode('UTF-8')

    bpassword = bytearray()
    bpassword = password.encode('UTF-8')

    logger = logging.getLogger('wc.controller')
    logger.info('Starting night function in telnetapi')
    logger.debug('calling telnet with following arguments: ' + user + ' ' + password + ' ' + targetip + ' ' + portnumber)

    tn = telnetlib.Telnet(targetip, portnumber)

    tn.write(buser + b"\n")
    tn.write(bpassword + b"\n")
    tn.write(b"\n")
    tn.write(b"time set night\n")
    tn.close()

    logger.debug('closing telnet')
    return
