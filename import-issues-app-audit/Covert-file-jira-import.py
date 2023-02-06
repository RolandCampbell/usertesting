# Test


import sys
import argparse
# import pandas
import os.path
from os import path

class BuildHTML:
	htmlLine = ""
	def __init__(self, bigpain, platform):
		self.lineToEdit = bigpain
		
		print( self.lineToEdit)

	def convertToHtml(self):
		print("in convert to html")
		self.htmlLine = self.lineToEdit.replace("\\","</div><div>")
		self.htmlLine = "<div>" + self.htmlLine.strip('\n') + "</div>"
		addLink1 = self.htmlLine.split('[')
		if len(addLink1) != 1: 
			addLink2 = addLink1[1].split( ']' )
			addLink3 = addLink2[0].split( '|')
			linkHTML = "<a href=" + "\"\"\""+ addLink3[1] +"\"\"\"" + ">" + addLink3[0] + "<a>"
			newHTMLLine = addLink1[0]  + linkHTML + addLink2[1]
			print(newHTMLLine)
			return (newHTMLLine)
		else:
			return self.htmlLine


class ImportFile:
	firstTime = True
	fileName = ""
	platform = ""
	def __init__(self, fileName):
		self.fileName = fileName
		print("in constructor" + self.fileName )

	def convertFile(self):
		
		
		with open(self.fileName, "r") as f:
			with open("fixedFile.csv", "w") as f1:
				for line in f:
					if self.firstTime:
						self.firstTime = False
						f1.write("Title,Work Item Type,Description\n")
						print("firsttime")
					else:
						strLine = line
						
						splitArray = strLine.split(',')
						
						if len(splitArray) > 3:
							bigpain = splitArray[3]
							bh = BuildHTML(bigpain, self.platform)

							writeLine = splitArray[1] + ",Issue," + bh.convertToHtml() +'\n'
							f1.write(writeLine)
							print("other times") 
				f1.close
				f.close 

		
def main():
	args = sys.argv[1:]
	print(args[1])
	if not path.exists(".\\" + args[1]):
		print("file " + str(args[1]) + "doesn't exist")
		sys.exit(1)
	fileName = args[1]	


	updateFile = ImportFile(fileName)
	print (updateFile.fileName)
	updateFile.convertFile()
	print ("after convert")

if __name__ == "__main__":
    main()
