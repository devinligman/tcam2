import numpy as np

testPoint = 1
runNumber = 1

class DataColumn:
    rawValue = -999
    euValue = -999
    columnWidth = -999
    precision = -999
    columnName = 'CODE'

    def __init__(self,columnName,columnWidth,precision):
        self.columnName = columnName
        self.columnWidth = columnWidth
        self.precision = precision

    def formatColumName(self):
        return ("{:>"+str(self.columnWidth)+"}").format(self.columnName)

    def formatEUValue(self):
        if(self.columnName == "CODE" ):
            return ('{0:>'+str(self.columnWidth)+'.' +str(self.precision) +'f}    ').format(float(self.euValue))
        else:
            return ('{0:>'+str(self.columnWidth)+'.' +str(self.precision) +'f}').format(float(self.euValue))

    def formatRawValue(self):
        if(self.columnName == "CODE"):
            return ('{0:>'+str(self.columnWidth)+'.' +str(self.precision) +'f}    ').format(float(self.rawValue))
        else:
            return ('{0:>'+str(self.columnWidth)+'.' +str(self.precision) +'f}').format(float(self.rawValue))



columns = [DataColumn("CODE",1,0),DataColumn("TP",5,0),DataColumn("LIFTR",10,3),DataColumn("DRAGR",10,3),DataColumn("SFR",10,3)]

columns[0].euValue = 0
columns[2].euValue = 122.512
columns[2].euValue = 52.5224
columns[2].euValue = 61.5424353

def begin():
    print("Data manger begun")


def saveColumns():
    print("Saving columns to file")

def loadColumns():
    print("Loading columns from file")
