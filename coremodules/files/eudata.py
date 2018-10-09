import os
import coredata.DataManager as dataManager
import coredata.TestController as testController

event_dispatcher = None


def setup():
    print("setup?")


def runNumberChanged(event):
    if runFileExists() == False:
        initRunFile()


def getRunFileLocation():
    runNumber = dataManager.runNumber
    tcamDir = testController.testDirectory + os.sep + 'TCAM' + os.sep
    return tcamDir + 'RUN_' + str(int(runNumber)).zfill(4) + '.EU'


def runFileExists():
    print(getRunFileLocation())
    return os.path.isfile(getRunFileLocation())


def initRunFile():
    file = open(getRunFileLocation() , 'a')
    file.write(':Test     = 9985\n')
    file.write(':Run      = 30\n')
    file.write('\'' + str(len(dataManager.columns)) + ' channels\n')
    file.write('\'')
    for column in dataManager.columns:
        file.write(column.formatColumName())
    # for columnName in dataManager.dataColumns[1:]:
    #    file.write('{:>6}'.format(columnName))
    file.write('\n')
    file.close()


def addRow():
    file = open(getRunFileLocation() , 'a')
    for column in dataManager.columns:
        file.write(column.formatEUValue())
    file.write('\n')
    file.close()
