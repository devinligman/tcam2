import coredata.TestController as testController
import coredata.DataManager as dataManager


# Begin core services
testController.begin()
dataManager.begin()

# testController.openPreviousTest(1540)
# testController.startNewTest(1541)


# sample module loading
import coremodules.files.eudata as eudata
eudata.setup()
eudata.addRow()


import endpoints.DataInput as DataInput
# DataInput.begin()
