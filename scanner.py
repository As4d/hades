import os
import re
import pathlib
from user import UserInfo

class Scanner():
    def __init__(self, obj):
        self.fileHelper = obj
        self.VulnerableFileNameFlags = 0
        self.VulnerableTextInFileFlags = 0
        self.PythonFilesAccessed = 0
    

    def findVulnerableFileNames(self, extension):
        temp = 0
        vulnerablestrings = [
            "password",
            "account",
            "statement",
            "bank",
            "passport",
            "drivers liscense",
            "pin",
        ]

        if extension in self.fileHelper.files.keys():
            for file in self.fileHelper.getFilesList(extension):
                temp = file[::-1].split("\\")[0]
                filename = temp[temp.find(".") + 1 :][::-1]
                for string in vulnerablestrings:
                    x = re.findall("(?i)({}):*s*".format(string), filename)
                    if x != []:
                        #print(x, file)
                        self.VulnerableFileNameFlags += 1
        else:          
            self.fileHelper.findAllFiles(extension)
            for file in self.fileHelper.getFilesList(extension):
                temp = file[::-1].split("\\")[0]
                filename = temp[temp.find(".") + 1 :][::-1]
                for string in vulnerablestrings:
                    x = re.findall("(?i)({}):*s*".format(string), filename)
                    if x != []:
                        #print(x, file)
                        self.VulnerableFileNameFlags += 1
        

    def findVulnerablitiesInTxt(self, file):
        sentences = [x.strip() for x in open(file, "r").readlines()]
        vulnerablestrings = [
            "password",
            "account",
            "statement",
            "bank",
            "passport",
            "drivers liscense",
            "pin",
        ]
        for sentence in sentences:
            for string in vulnerablestrings:
                x = re.findall("(?i)({}):*s*".format(string), sentence)
                if x != []:
                    pass # print(x)

    def infectPyFiles(self):  # mimics self replication
        for file in self.fileHelper.getFilesList("py"):
            try:
                FH = open(file, "a")
                self.PythonFilesAccessed += 1
                print(self.PythonFilesAccessed)
            except:
                pass
    
    def getVulnerableFileNameFlags(self):
        return self.VulnerableFileNameFlags
    
    def setVulnerableFileNameFlags(self, item):
        self.VulnerableFileNameFlags = item
    
    def resetVulnerableFileNameFlags(self):
        self.VulnerableFileNameFlags = 0
    
    def getPythonFilesAccessed(self):
        return self.PythonFilesAccessed
    
    def setPythonFilesAccessed(self, item):
        self.PythonFilesAccessed = item