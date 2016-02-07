## Dear reader
## Thanks for your interest in this software
## This software is free to use and modify
## There is currently no licence attached to this software
## I assume no responsibility with regards to the utilisation of this software
## No creepers, or any other mobs, were hurt during the realisation or utilisation of this software
##
## Gery Ducatel
##

import logging          # a logger library
import argparse         # an argument parser library (to read options with command lines)
import configparser     # a config initialisation library (to load config files)
import os               # a library used to check files on the system
import re               # Oh yeah, that's right, import regular expression, c'mon baby

from cmdline import launch
from light import foreverlight

# start
# I want the ability to start with specific target IP address for the weather state REST API server, and port (default being 127.0.0.1 and 8080)
# I want the ability to start with a different log file name
# I want the ability to start with a different initialisation file name
# I want the ability to configure the state reading frequency (how often the rain/light sensors are read)
# The logger needs an optional argument to set the log level
# The final argument is the IP address of the minecraft server (mandatory)








def main():

    ## Start initialisation which includes reading input arguments and logging

    loginit()
    
    initialise()

    return
    

def loginit():
    # if no log directory exist create one
    # hard wired

    directory = './log'
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    # declare the log file name - hard wired

    logger = logging.getLogger('wc.controller')
    fh = logging.FileHandler(filename = directory+'/weathercraft.log')
    logging.basicConfig(level = logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    
    logger.addHandler(fh)
    


## Initialise function
def initialise():


    logger = logging.getLogger('wc.controller')

    # start parsing arguments
    parser = argparse.ArgumentParser(description='Start the weather craft command module which sends external sensor information to the designated minecraft server (target). Note readings from the command line argument passing override values in the default config file wcconfig.ini')

    # parser action means: store TRUE in variable --<optionname>
    parser.add_argument('target', metavar = 'IP', help = 'IP address of the server running Minecraft', type = str)
    parser.add_argument("-p", "--port", help = "Port to send requests to the server running Minecraft (default value in wcconfig.ini: 25564", type = int)
    parser.add_argument("-v", "--verbose", action = "store_true", help = "increase output verbosity")
    parser.add_argument("-ll", "--loglevel", help = "Modify the log level between CRITICAL ERROR WARNING INFO DEBUG NOTSET", type = str)
    parser.add_argument("-c", "--configfile", help = "Designate a new config file", type = str)
    parser.add_argument("-f", "--frequency", default = 60, help = "Number of seconds between two sensor state readings - default is 10 seconds", type = int, choices=range(1, 60))
    parser.add_argument("-u", "--user", help = "User name for the minecraft server API", type = str)
    parser.add_argument("-pwd", "--password", help = "password for the minecraft server API", type = str)
    parser.add_argument("-lip", "--localip", default = '127.0.0.1', help = "local IP address default 127.0.0.1", type = str)
    parser.add_argument("-lp", "--localport", default = 8080, help = "local port default 8080", type = int)
    parser.add_argument("-t", "--test", action = "store_true", help = "Run in test mode with command line input")
    parser.add_argument("-dn", "--daynight", action  = "store_true", help = "Read daylight input from external sensor")

    args = parser.parse_args()


    logger.info('WeatherCraft weather state reader and forward to Minecraft server is starting...')
    
    logger.debug('Kicking off the - initialise - method')


    
    ## catch input validation
    # valid entries for log level
    if args.loglevel:
        if args.loglevel.upper() not in ('CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET'):
            logging.error("not a valid log level: " + args.loglevel)
        else:
            logger.setLevel(args.loglevel.upper())
            logging.info('Setting log level to: ' + args.loglevel.upper())


    ## set log level immediately
    #
    # faulty code:
    #logging.debug('parameters passed over to the initialise method are: ' + args)
    # Error thrown
    # TypeError: Can't convert 'Namespace' object to str implicitly
    
    # log a debug statement with all arguments
    # NTS: not sure this is the best way...
    if logger.getEffectiveLevel() <= 10:
        for arg, value in vars(args).items():
            logger.debug('Argument no ' + ' : ' + str(arg) +' = ' + str(value))
            #print('Argument no ' + ' : ' + str(arg) +' = ' + str(value))

    ## validate target address
    ipreg = re.compile(r"(\d{1,3}\.{1}){3}\d{1,3}")
    ipmatch = ipreg.match(args.target)
    
    if ipmatch:
        logger.debug('The target address is: ' + args.target)
        #global targetip
        targetip = args.target
    else:
        # TODO learn how to use additional arguments *args and **kwargs for error logging
        logger.error('The target address IP does not have the right format: ' + args.target)

    ## validate port number
    if args.port:
        if 0 < args.port and args.port < 65536:
            logger.debug('The port number is: ' + str(args.port))
            #global portnumber
            portnumber = args.port
        else:
            logger.error('The selected port ' + args.port + ' is invalid, must be between 0 and 65536')
                      

    if args.frequency:
        if (0 < args.frequency) and (args.frequency <= 600):
            logger.debug('The frequency is : ' + str(args.frequency))
            #global frequency
            frequency = args.frequency
        else:
            frequency = args.frequency
            logger.debug('frequency default to ' + str(args.frequency))

    if args.user:
        #global user
        user = args.user

    if args.password:
        #global password
        password = args.password

    ## validate local target address
    #ipreg = re.compile(r"(\d{1,3}\.{1}){3}\d{1,3}")
    ipmatch = ipreg.match(args.localip)
    
    if ipmatch:
        logger.debug('The target address is: ' + args.target)
        #global localtargetip
        localtargetip = args.localip
    else:
        # TODO learn how to use additional arguments *args and **kwargs for error logging
        logger.error('The local target address IP does not have the right format: ' + args.localip)

    ## validate local port number
    if args.localport:
        if 0 < args.localport and args.localport < 65536:
            logger.debug('The port number is: ' + str(args.port))
            #global localportnumber
            localportnumber = args.localport
        else:
            logger.error('The selected port ' + args.port + ' is invalid, must be between 0 and 65536')

    if args.configfile:
        if not os.path.isfile(args.configfile):
            logger.error('The configuration file does not exist: ' + args.configfile)
        else:
            config = configparser.ConfigParser()
            configfile = args.configfile
            config.read_file(open(configfile))
            localtargetip = config.get('raspberry.sensor', 'ip')
            localportnumber = config.get('raspberry.sensor', 'port')
            targetip = config.get('raspberry.minecraft', 'ip')
            portnumber = config.get('raspberry.minecraft', 'port')
            user = config.get('raspberry.minecraft', 'user')
            password = config.get('raspberry.minecraft', 'password')
            frequency = config.get('raspberry.minecraft', 'frequency')


    if not user:
        logger.error('User is not defined')
    else:
        logger.debug('final config user: ' + user)
        
    if not password:
        logger.error('password is not defined')
    else:
        logger.debug('final config password: ' + password)
        
    if not localtargetip:
        logger.error('local target ip is not defined')
    else:
        logger.debug('final config local IP: ' + localtargetip)
        
    if not localportnumber:
        logger.error('local target port number is not defined')
    else:
        logger.debug('final config local port: ' + str(localportnumber))
        
    if not targetip:
        logger.error('Minecraft server target IP is not defined')
    else:
        logger.debug('final config minecraft target IP: ' + targetip)
        
    if not portnumber:
        logger.error('Minecraft server port number is not defined')
    else:
        logger.debug('final config minecraft port number: ' + str(portnumber))
        
    if not frequency:
        logger.error('Refresh frequency is not defined')
    else:
        logger.debug('final config frequency: ' + str(frequency))



    #
    # If test flag is up ask for user input (usually for testing)
    #
    if args.test:
        logger.debug('Launching a test with the following parameters: ' + user + ' ' + password + ' ' + targetip + ' ' + portnumber)
        launch(user, password, targetip, portnumber)

    if args.daynight:
        logger.debug('Starting exernal reading for light from sensor')
        foreverlight(user, password, targetip, portnumber)


    
    return


main()

## dev main start
## Dead code, this was for starting the programme from IDLE, but I gave up on this. I am keeping this for reference.
#if __name__ == "__main__":
#    if False: # not testing?
#        sys.exit(mymain())
#    else:
#        # Test/sample invocations (can test multiple in one run)
#        #devmain()
#        devmain("mytarget", "--loglevel=debug", "-v")
## dev main end


#config = configparser.ConfigParser()
#configFile = 'myconfig.ini'
#config.read(configFile)

#config.sections()

#user = config.get('raspberry.minecraft', 'user')
#password = config.get('raspberry.minecraft', 'password')
#ip = config.get('raspberry.minecraft', 'ip')
#port = config.get('raspberry.minecraft', 'port')

## convert string to bytes
#buser = bytes(user, 'utf-8')
#buser = user.encode('utf-8')

## print bytes as string
#print ("hello "+buser.decode('utf-8'))
#print ("hello "+str(buser, 'utf-8'))

