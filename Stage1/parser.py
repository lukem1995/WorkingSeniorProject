#This is a class to parse the output files from the injection class

class Parser():

	def __init__(self):
		self.dbsFile = None
		self.tblFile = None
	
	#Method to parse databases list
	def dbsParse(self, myFile):
		self.dbsFile = myFile
		file = open(self.dbsFile,"r")
		for line in file:
			print line,
		
	#Method to parse tables list
	def tblParse(self, myFile):
		#To be written
		self.tblFile = myFile
		file = open(self.tblFile,"r")
                for line in file:
                        print line,
 
