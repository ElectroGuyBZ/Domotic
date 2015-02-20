# -*- coding: utf-8 -*-
################################################
#            serial Rx INTERFACE V1.0          #
#                                              #
#   written by Qi TANG             29.04.2014  #
#   modified by Mickaël CAPTANT    29.05.2014  #
#                                              #
# Description: Read data from Serial port      #
#                                              #
################################################

## HOW TO TEST
## In serial port COM1 tape that:
    ## $.00-01.02-02.R11.R21.R30.#

##import all librairies we needed
import serial
import subprocess
from ConfigParser import SafeConfigParser
import time

##Initiation of the variables with .conf file
def  initVariables():
    ##open the conf file
    cfg = SafeConfigParser()
    cfg.read('config.ini')
    ##Define Serial Port
    global serialPort
    global baud
    global shellCommand
    global serial1
    global commandConfig
    serialPort = cfg.get('SERIAL_PORT', 'serialPort')
    baud = cfg.get('SERIAL_PORT', 'baud')
    shellCommand = cfg.get('SCRIPT', 'domoticServer')
    serial1 = serial.Serial(serialPort, baud)
    ##Define START and END character
    global END
    END = cfg.get('ENCODE', 'END')
    ##Define variable for Server command
    commandConfig = cfg.get('CONFIG','commandSerial')
    ##Define file for data logging
    global log
    log = cfg.get('LOG', 'logRx')
    #file for command log
    global logCommand
    logCommand = cfg.get('LOG', 'logCommand')

def logger(dataToLog,fileToLog):
    logFile = open(fileToLog, 'a')
    logBuffer = time.strftime("%d %m %Y %H:%M:%S") + ">" + dataToLog + "\n"
    logFile.write(logBuffer)

##Read data from Serial port and make a string
def serialEvent():
    ##Define global variable
    global serial1
    global data
    data = ""
    ##Define local variable
    StringComplete = False
    char = ""
    ##Loop for a complete string
    while(StringComplete == False):
        while(char != END):##wait for a END character
            char = serial1.read()
            data = data + char
            if char == END:
                StringComplete = True
                return data

##Main fonction
def main():
    initVariables()
    serial1.close()
    serial1.open()
    global shellCommand
    ##make a loop
    while(1):
        RxBuffer = serialEvent()
        ##Log the data receiving
        logger(RxBuffer,log)
        RxBuffer = "1." + RxBuffer
        logger(RxBuffer,logCommand)
        ##Only for debugging
        #print "RxBuffer: " + RxBuffer
        #argument = "python" + " " + shellCommand + ' ' + commandConfig + " " + RxBuffer
        ##Call Server program with RxBuffer variable
        #subprocess.Popen(shellCommand.split(), stdout=subprocess.PIPE)
        ##Only for debugging
        #commandToSend = subprocess.Popen(argument.split(), stdout=subprocess.PIPE)
        #commandToSend = commandToSend.stdout.read() + "\r"
        #print commandToSend
        ##Clear variables
        shellCommand = ""
        dataBuffer = ""
        RxBuffer = ""

if __name__ == "__main__":
    main()