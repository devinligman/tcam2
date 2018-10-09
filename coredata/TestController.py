from coredata.ConfigFile import ConfigFile

import os

tcamConfig = ConfigFile("config/TCAM2Settings.ini")
testDirectory = None;
testConfig = None;

def begin():
    print("Launching TCAM, opening previous test")
    testNumber = tcamConfig.read_config("status","test_number")
    if testNumber != 0:
        if openPreviousTest(testNumber) == False:
            startNewTest(testNumber)

def startNewTest(testNumber):
    testsDirectory = tcamConfig.read_config("environment","tests_directory")
    testNameFormat = tcamConfig.read_config("environment","test_format")
    tn = str(int(testNumber)).zfill(testNameFormat.count("?"))
    formattedTestNum = testNameFormat.replace("?" * testNameFormat.count("?"), tn)
    print("Starting new test number", formattedTestNum)
    possibleTestDirectory = testsDirectory + os.sep + formattedTestNum
    #check if test exists
    if os.path.isdir(possibleTestDirectory):
        print("Test already exists")
        return False

    #try to create new test and TCAM folders
    try:
        os.mkdir(possibleTestDirectory)
        os.mkdir(possibleTestDirectory + os.sep + 'TCAM')
    except Error:
        print("Error creating folder")
        return False

    #update globals
    global testDirectory, testConfig
    testDirectory = testsDirectory + os.sep + formattedTestNum
    testConfig = ConfigFile(testDirectory + os.sep + 'TCAM' + os.sep + 'testSettings.ini')
    testConfig.set_config('test_info','run_number',1)
    return True

def openPreviousTest(testNumber):
    testNameFormat = tcamConfig.read_config("environment","test_format")
    testsDirectory = tcamConfig.read_config("environment","tests_directory")
    print("Opening with test", testNumber)
    tn = str(int(testNumber)).zfill(testNameFormat.count("?"))
    formattedTestNum = testNameFormat.replace("?" * testNameFormat.count("?"), tn)
    global testDirectory, testConfig
    testDirectory = testsDirectory + os.sep + formattedTestNum
    if not os.path.isdir(testDirectory):
        print("Test folder does not exist")
        return False
    print("Reading test settings")
    testConfig = ConfigFile(testDirectory + os.sep + 'TCAM' + os.sep + 'testSettings.ini')
