import configparser
import os

class ConfigFile:
    def __init__(self,configFileLocation):
        self.config = configparser.ConfigParser()
        if os.path.isfile(configFileLocation):
            self.config.read(configFileLocation)
        else:
            with open(configFileLocation, 'w') as configfile:
                self.config.write(configfile)
        self.configFileLocation = configFileLocation

    def read_config(self,section,key):
        if self.config.has_section(section) == False:
            return None
        if self.config.has_option(section, key) == False:
            return None
        return self.config[section][key]

    def set_config(self,section,key, value):
        if self.config.has_section(section) == False:
            self.config.add_section(section)
        self.config[section][key] = str(value)
        with open(self.configFileLocation, 'w') as configfile:    # save
            self.config.write(configfile)
