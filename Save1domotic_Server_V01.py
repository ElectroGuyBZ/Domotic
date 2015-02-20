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
    dateFile= open(logDate,'r')
    date = dateFile.read()
    dateFile.close()
    commandFile = open(logCommand, 'r')
    commandFileData = commandFile.readlines()
    #lenLine = len(commandFileData)
    lenLine = sum([1 for line in commandFileData])
    print lenLine
    if date == "":
        commandSplit = commandFileData[0].split('>',)
        commandToExecute = commandSplit[1]
        date = commandSplit[0]
        dateFile = open(logDate,'w')
        dateFile.write(date)
        return commandToExecute
    for line in range (0,(lenLine)):
        commandSplit = commandFileData[line].split('>',)
        if commandSplit[0] == date:
            print "line 0"
            if lenLine < line + 1:
                print "ERROR"
                commandToExecute = "ERROR"
                return commandToExecute
            elif lenLine != line and lenLine < line:
                print line
                commandSplit = commandFileData[line + 1].split('>',)
                commandToExecute = commandSplit[1]
                date = commandSplit[0]
                dateFile = open(logDate,'w')
                dateFile.write(date)
                return commandToExecute
            else:
                print "???"

def commandAnalyser(commandToExecute):
    global typeOfData

    if commandToExecute == "":
        commandDecrypted =="ERROR"
        return commandDecrypted
    commandToExecuteSplit = commandToExecute.split('.',)
    commandToExecuteLength = len(commandToExecuteSplit)
    if commandToExecuteLength >=5:
        typeOfData = commandToExecuteSplit[0]
        start = commandToExecuteSplit[1]
        if typeOfData == commandSerial:
            receiver = commandToExecuteSplit[2]
            emitter = commandToExecuteSplit[3]
        else:
            receiver = commandToExecuteSplit[3]
            emitter = commandToExecuteSplit[2]
        command1 = commandToExecuteSplit[4]
        if commandToExecuteLength == 5:
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
                print commandToExecute
                commandDecrypted = commandAnalyser(commandToExecute)
                print "decrypt: " + commandDecrypted
                if typeOfData == commandSerial:
                    shellCommand = "python" + ' ' + domoticSerialTx + ' ' + commandDecrypted
                    subprocess.Popen(shellCommand, shell=True)
                if typeOfData == commandInterface or typeOfData == commandWeb:
                    shellCommand = "python" + ' ' + domoticGenerator + ' ' + commandDecrypted
                    subprocess.Popen(shellCommand, shell=True)

if __name__ == "__main__":
    main()