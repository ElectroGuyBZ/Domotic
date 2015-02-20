# -*- coding: utf-8 -*-
################################################
#            serial Rx INTERFACE V1.0          #
#                                              #
#   written by Qi TANG             29.04.2014  #
#   modified by Mickaël CAPTANT    29.05.2014  #
#                                              #
# Description: Encode and Decode the data      #
#                                              #
################################################

## HOW TO TEST
## in command line , tape that:
    ## python data_Encrypter_V01.py 1 S0N1 S2N2 RELAY1ON RELAY2OFF RELAY3ON
    ##        OR
    ## python data_Encrypter_V01.py 2 00-01 02-02 R11 R12 R21

#import all librairies we needed
import csv
import sys
import time
from ConfigParser import SafeConfigParser

# Initiation of the variables with .conf file
def initVariables():

    #open the conf file
    cfg = SafeConfigParser()
    cfg.read('config.ini')

    #Define Serial Port
    global serialPort
    serialPort = cfg.get('SERIAL_PORT', 'serialPort')

    #Define CSV files
    global database1
    database1 = cfg.get('DATABASE', 'command')
    global address
    address = cfg.get('DATABASE', 'address')

    #Define START and END character
    global START
    START = cfg.get('ENCODE', 'START')
    global END
    END = cfg.get('ENCODE', 'END')

    #Define LINUX MAC_Address
    global linuxMac
    linuxMac = cfg.get('LINUX_ADDRESS', 'linuxMac')

    #Delimiter for CSV files
    global delimiter
    delimiter = cfg.get('DATABASE', 'delimiter')

    #Column to found in command line
    global commandLineData
    commandLineData = cfg.get('COLUMN_INFO', 'commandLineData')
    global commandLineCommand
    commandLineCommand = cfg.get('COLUMN_INFO', 'commandLineCommand')
    #Column for comment
    global comment
    comment = cfg.get('COLUMN_INFO', 'comment')

    #file for log
    global log
    log = cfg.get('LOG', 'logServer')



def Search_Column(tab,key):
    columnLengh = len(tab[0])
    columnSearch = 0
    columnFLAG1 = False
    for sublist in tab:
        for column in range(0, columnLengh):
            if sublist[column] == key:
                columnSearch = column
                columnFLAG1 = True
                return columnSearch
    if columnFLAG1 is False:
                columnSearch = -1
                return columnSearch

def Data_Search(database):
    #create a list of lists:
    listOfData = list(csv.reader(open(database, 'rb'), delimiter=delimiter))
    return listOfData

def getData(database,typeOfSearch, search):

    global commandLineData
    global commandLineCommand
    global comment

    #Define list of Data
    data = Data_Search(database)
    #read a cell:
    #cell =data[0][1]
    #Define length of data list
    columnLengh = len(data[0])

    #Define variables
    cell = ""
    line = -1

    #Define FLAG
    getDataFLAG = False

    #in terminal
    #sub = raw_input("type of your research:")

    #make UPPER for search
    #sub = sub.upper()
    search = search.upper()
    commandLineData = commandLineData.upper()
    commandLineCommand = commandLineCommand.upper()

    #Search type of data in a list of data
    #column_search = Search_column(sub)
    if typeOfSearch == '2' or typeOfSearch == '3':
        column_wanted = Search_Column(data, commandLineData)
    elif typeOfSearch == '1':
        column_wanted = Search_Column(data, commandLineCommand)
    column_comment = Search_Column(data, comment)


    #Get result:
    if  column_wanted != -1:
        for sublist in data:
            line = line + 1
            for column_search in range(0, columnLengh):
                if sublist[column_search] == search:
                    cell = data[line][column_wanted]
                    comment = data[line][column_comment]
                    getDataFLAG = True



        if getDataFLAG:
            # save data in the variable "Code"
            Data = cell
            return Data

        else:
            #only for debug
            #print "error during the research..."
            #print " no data found for",search
            Data = "ERROR"
            return Data

def commandToSend(receiverMAC_Address,emitterMAC_Address, data1, data2, data3):
    #command = [START,Rx,Tx,Function,cell,END]
    command = START + '.' + receiverMAC_Address + '.' + emitterMAC_Address + '.'

    if data1 != "":
        command = command + data1 + '.'
    if data2 != "":
        command = command + data2 + '.'
    if data3 != "":
        command = command + data3 + '.'
    command = command + END
    return command

def commandLine():
    #Define FLAGs for ERROR
    global errorFLAGData
    global errorFLAGTarget
    global errorFLAGEmitter
    global errorFLAG
    global DataCommand
    global DataCommand2
    global DataCommand3
    global Target
    global Emitter
    global database1
    global address
    errorFLAG = True
    errorFLAGData = False
    errorFLAGTarget = False
    errorFLAGEmitter = False
    DataCommand = ""
    DataCommand2 = ""
    DataCommand3 = ""
    Target = ""
    Emitter = ""
    lenArg = len(sys.argv)

    if lenArg == 1:
        Target = getData(address,raw_input("Who is the target:"))
        Emitter = getData(address,raw_input("Who is the emitter:"))
        DataCommand = getData(database1,raw_input("Who is the first command:"))
        DataCommand2 = getData(database1,raw_input("Who is the second command:"))
        DataCommand3 = getData(database1,raw_input("Who is the third command:"))

    if lenArg >= 2:
        #Search in command line
        Search = sys.argv[1]

        if lenArg >= 3:
            #target in command line
            Target = getData(address, Search, sys.argv[2])
        if lenArg >= 4:
            #Emitter in command line
            Emitter = getData(address, Search, sys.argv[3])
        if lenArg >= 5:
            #data in command line
            DataCommand = getData(database1, Search, sys.argv[4])
        if lenArg >= 6:
            DataCommand2 = getData(database1, Search, sys.argv[5])
        if lenArg >= 7:
            DataCommand3 = getData(database1, Search, sys.argv[6])

    if DataCommand == "ERROR" or DataCommand == "":
        errorFLAGData = True

    elif Target == "ERROR" or Target == "":
        errorFLAGTarget = True
    elif Emitter == "ERROR" or Emitter == "":
        errorFLAGEmitter = True
    else:
        errorFLAG = False

def ControlError():
    if errorFLAGData:
        error = "ERROR201"
    elif errorFLAGTarget:
        error = "ERROR202"
    elif errorFLAGEmitter:
        error = "ERROR203"
    return error

def logger(dataToLog,fileToLog):
    logFile = open(fileToLog, 'a')
    logBuffer = time.strftime("%d %m %Y %H:%M:%S") + ">" + dataToLog + "\r"
    logFile.write(logBuffer)

def main():
    initVariables()
    commandLine()
    if errorFLAG is False:
        ##Only for debugging
        #print "Target: " + Target
        #print "Emitter:" + Emitter
        #print "DataCommand: " +DataCommand
        #print "DataCommand2: " +DataCommand2
        #print "DataCommand3: " +DataCommand3
        ##Construction of the trame
        toSend = commandToSend(Target,Emitter, DataCommand, DataCommand2, DataCommand3)
    else:
        toSend = ControlError()


    logger(toSend,log)
    print toSend

if __name__ == "__main__":
    main()
