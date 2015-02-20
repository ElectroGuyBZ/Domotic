# -*- coding: utf-8 -*-
################################################
#            Domotic Server V1.0               #
#                                              #
#   written by Qi TANG             29.04.2014  #
#   modified by Mickaël CAPTANT    30.05.2014  #
#                                              #
# Description: Main program of the SERVER      #
#                                              #
################################################

import subprocess
import sys
import time
from ConfigParser import SafeConfigParser

# Initiation of the variables with .conf file
def  initVariables():
    #open the conf file
    cfg = SafeConfigParser()
    cfg.read('config.ini')
    #file for log
    global log
    log = cfg.get('LOG', 'logServer')
    #file for command log
    global logCommand
    logCommand = cfg.get('LOG', 'logCommand')
    #file for date log
    global logDate
    logDate = cfg.get('LOG', 'logDate')
    #configuration of data
    global commandSerial
    commandSerial = cfg.get('CONFIG', 'commandSerial')
    global commandInterface
    commandInterface = cfg.get('CONFIG', 'commandInterface')
    global commandWeb
    commandWeb = cfg.get('CONFIG', 'commandWeb')
    #scripte to launch
    global domoticEncrypter
    domoticEncrypter = cfg.get('SCRIPT', 'domoticEncrypter')
    global domoticGenerator
    domoticGenerator = cfg.get('SCRIPT', 'domoticGenerator')
    global domoticSerialTx
    domoticSerialTx= cfg.get('SCRIPT', 'domoticSerialTx')
    global domoticSerialRx
    domoticSerialRx= cfg.get('SCRIPT', 'domoticSerialRx')
    #Define Variables
    global typeOfData

def logger(dataToLog,fileToLog):
    logFile = open(fileToLog, 'a')
    logBuffer = time.strftime("%d %m %Y %H:%M:%S") + ">" + dataToLog + "\r"
    logFile.write(logBuffer)

def logAnalyser():
    lineDate =""
    count = 0
    dateFile= open(logDate,'r')
    date = dateFile.read()
    dateFile.close()
    commandFile = open(logCommand)
    if date == "":
        #print "no date"
        commandFileData = commandFile.readlines()
        if commandFile.read() != "":
            commandSplit = commandFileData[0].split('>',)
            commandToExecute = commandSplit[1]
            date = commandSplit[0]
            dateFile = open(logDate,'w')
            dateFile.write(date)
            return commandToExecute
    with open(logCommand,'r') as commandFile:
        #lines = commandFile.readlines()
        for line in commandFile:
            #print line
            lineSplit = line.split('>',)
            lineDate = lineSplit[0]
            if lineDate > date and lineDate != "":
                commandToExecute = lineSplit[1]
                date = lineSplit[0]
                #print "date is >" + date
                dateFile = open(logDate,'w')
                dateFile.write(date)
                return commandToExecute
    commandFile.close()

def commandAnalyser(commandToExecute):
    global typeOfData

    if commandToExecute == "":
        commandDecrypted =="ERROR301"
        return commandDecrypted
    commandToExecuteSplit = commandToExecute.split('.',)
    commandToExecuteLength = len(commandToExecuteSplit)
    #print commandToExecuteLength
    if commandToExecuteLength >=6:
        typeOfData = commandToExecuteSplit[0]
        start = commandToExecuteSplit[1]
        if typeOfData == commandSerial:
            receiver = commandToExecuteSplit[2]
            emitter = commandToExecuteSplit[3]
        else:
            receiver = commandToExecuteSplit[3]
            emitter = commandToExecuteSplit[2]
        command1 = commandToExecuteSplit[4]
        if commandToExecuteLength == 6:
            command2= ''
            command3= ''
            end = commandToExecuteSplit[5]
        elif commandToExecuteLength ==7:
            command2 = commandToExecuteSplit[5]
            command3 =''
            end = commandToExecuteSplit[6]
        elif commandToExecuteLength ==8:
            command2 = commandToExecuteSplit[5]
            command3 = commandToExecuteSplit[6]
            end = commandToExecuteSplit[7]
    elif commandToExecuteLength <4:
        commandToExecuteSplit = "ERROR"
        return commandToExecuteSplit

    command = command1 + ' ' + command2 + ' ' + command3
    shellCommand = "python " + domoticEncrypter + ' ' + typeOfData + ' ' \
    + emitter + ' ' + receiver + ' ' + command
    commandDecrypted = subprocess.check_output(shellCommand, shell=True)
    return commandDecrypted

def main():
    initVariables()
    shellCommand = "python" + ' ' + domoticSerialRx
    #subprocess.Popen(shellCommand, shell=True)
    while(1):
        commandToExecute = logAnalyser()
        #print commandToExecute
        if commandToExecute is not None :
            #if commandToExecute != "ERROR":
                #print commandToExecute
                commandDecrypted = commandAnalyser(commandToExecute)
                print "decrypt: " + commandDecrypted
                if typeOfData == commandSerial:
                    shellCommand = "python" + ' ' + domoticGenerator + ' ' + commandDecrypted
                    subprocess.Popen(shellCommand, shell=True)
                if typeOfData == commandInterface or typeOfData == commandWeb:
                    shellCommand = "python" + ' ' + domoticSerialTx + ' T' + commandDecrypted
		    subprocess.Popen(shellCommand, shell=True)

if __name__ == "__main__":
    main()
