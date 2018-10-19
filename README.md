# tcam2
Simple data acquisition and test controller

#Code Structure
main.py - main python file that starts tcam2
coredata/
  ConfigFile.py - reusable configuration file manager
  DataManager.py -
  TestController.py -
coremodules/
  files/
    eudata.py
    csvdata.py
coreui/
  TBD
endpoints/
  DataInput.py
  DataStreaming.py
  RemoteControl.py


#File Structure
tests/
  UW2012/
    TCAM/
      RUN_0001.EU
      RUN_0002.EU
      RUN_0003.EU
      RUN_0004.EU
      RUN_0005.EU
      TestSettings.ini
      Flags.csv
    runs.csv - created by RunLog2
