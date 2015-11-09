## Dear reader
## Thanks for your interest in this software
## This software is free to use and modify
## There is currently no licence attached to this software
## I assume no responsibility with regards to the utilisation of this software
## No zombies were hurt during the realisation or utilisation of this software
##
## Géry Ducatel
##

import logging          # a logger library
import argparse         # an argument parser library (to read options with command lines)
import configparser     # a config initialisation library (to load config files)
import os               # a library used to check files on the system
import re               # Oh yeah, that's right, import regular expression, c'mon baby

# start
# I want the ability to start with specific target IP address for the weather state REST API server, and port (default being 127.0.0.1 and 8080)
# I want the ability to start with a different log file name
# I want the ability to start with a different initialisation file name
# I want the ability to configure the state reading frequency (how often the rain/light sensors are read)
# The logger needs an optional argument to set the log level
# The final argument is the IP address of the minecraft server (mandatory)


def main():

    ## Start initialisation which includes reading input arguments and logging
    initialise()

    return
    


## Initialise function
def initialise():

    directory = './log'
    
    if not os.path.exists(directory):
        logging.debug('creating log directory: '+directory)
        os.makedirs(directory)
        logging.debug('created log directory')
        
    # declare the log file name - hard wired
    logging.basicConfig(filename=directory+'/weathercraft.log')

    logging.info('WeatherCraft weather state reader and forward to Minecraft server is starting...')
    
    logging.debug('Kicking off the - initialise - method')
    logger = logging.getLogger('wc.controller')

    # if no log directory exist create one
    # hard wired

    # start parsing arguments
    parser = argparse.ArgumentParser(description='Start the weather craft command module which sends external sensor information to the designated minecraft server (target). Note readings from the command line argument passing override values in the default config file wcconfig.ini')

    # parser action means: store TRUE in variable --<optionname>
    parser.add_argument('target', metavar = 'IP', help = 'IP address of the server running Minecraft', type = str)
    parser.add_argument("-p", "--port", help = "Port to send requests to the server running Minecraft (default value in wcconfig.ini: 25564", type = int)
    parser.add_argument("-v", "--verbose", action = "store_true", help = "increase output verbosity")
    parser.add_argument("-ll", "--loglevel", help = "Modify the log level between CRITICAL ERROR WARNING INFO DEBUG NOTSET", type = str)
    parser.add_argument("-c", "--configfile", help = "Designate a new config file", type = str)
    parser.add_argument("-f", "--frequency", help = "Number of seconds between two sensor state readings - default is 10 seconds", type = int)

    args = parser.parse_args()


    
    ## catch input validation
    # valid entries for log level
    if loglevel in args:
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
            logging.debug('Argument no ' + ' : ' + str(arg) +' = ' + str(value))
            print('Argument no ' + ' : ' + str(arg) +' = ' + str(value))

    ## validate target address
    ipreg = re.compile(r"(\d{1,3}\.{1}){3}\d{1,3}")
    ipmatch = ipreg.match(args.target)
    if ipmatch:
        logging.debug('The target address is: ' + args.target)
    else:
        # TODO learn how to use additional arguments *args and **kwargs for error logging
        logging.error('The target address IP does not have the right format: ' + args.target)

    ## validate port number
    if port in args:
        if 0 < args.port and args.port < 65536:
            logging.debug('The port number is: ' + port)
        else:
            logging.error('The selected port ' + args.port + ' is invalid, must be between 0 and 65536')
                      
    
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


