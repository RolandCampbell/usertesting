import sys
import argparse
import csv

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
        self.fileName = fileName
        self.platform = platform
        print("in constructor")
    def convertFile(self):
        firstTime = True
        print("convert file")
        link = open(self.fileName)
        writeFile = open(".\\fixedfile.csv", "w")
        soup = BeautifulSoup(link.read(),features="html.parser")    
        soup.prettify
        print(soup.title)
        if firstTime:
            print("first time")
            writeFile.write("Issue Type,Summary,Severity,Description,User Journey\n")
            writeFile.close
            firstTime = False
        
        print("not first time")
          

        for table in soup.find_all('table', {'class': 'comments-table'}):
            print(table)  
            print(table.find('th').text) 
                

            p = table.find('p', {'class': 'comment-body'}).text
            print(p)

            


       
        writeFile.close

           
        
            


        


def main():
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

if __name__ == "__main__":
    main()
