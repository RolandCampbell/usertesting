import sys
import argparse
import csv
# import panda
import os.path
from os import path
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

class ImportFile:
    firstTime = True
    fileName = ""
    platform = ""
    def __init__(self, fileName, platform):
        self.fileName = args.fileName
        self.platform = args.platform
        print("in constructor")
    def convertFile(self):
        firstTime = True
        print("convert file")
        link = open(self.fileName)
        writeFile = open(".\\fixedfile.csv", "w")
        soup = BeautifulSoup(link.read(), features="lxml")
        soup.prettify
        print(soup.title)
        if firstTime:
            print("first time")
            writeFile.write("Issue Type,Summary,Severity,Description,User Journey\n")
            writeFile.close
            firstTime = False
        
        print("not first time")
        areaWrappers = soup.find_all("div", class_="area-wrapper")
   

        for areaWrapper in areaWrappers:
            # print(areaWrapper)
            print('\n')
            aqaLinks = areaWrapper.find_all('a', href = True)
            aqaDescs = areaWrapper.find_all("section", class_="markdown")
            aqaTitle = areaWrapper.find_all("h6")
            aqaName = areaWrapper.find_all("h5")
            writeFile = open(".\\fixedfile.csv", "a")

            
            for i in range(len(aqaLinks)):
                link = str(aqaLinks[i]['href'])
                descs = str(aqaDescs[i].find('p').getText())
                title = str(aqaTitle[i].getText())
                name = str(aqaName[i].getText())
                writeFile.write(("bug,\"" + name + " " + title + "\",,\"" + link + "," + descs + "\"\n"))
                print(("bug,\"" + name + " " + title + "\",,\"" + link + "," + descs + "\"\n"))

            print("   \n")
        writeFile.close

           
        
            


        



parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-p', action="store", dest="platform", choices=["jira"],default="jira", help=("only jira suported at this time"))
parser.add_argument('-f', action="store", dest="fileName", required=True)   
args = parser.parse_args()
if not path.exists(args.fileName):
	print("file " + str(args.fileName) + "doesn't exist")
	sys.exit(1)
updateFile = ImportFile(args.fileName, args.platform)
print (updateFile.platform)
updateFile.convertFile()
print ("after convert")