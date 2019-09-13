from injection import Injection
from parser import Parser
from fetcher import Fetcher

#Get login Url
#mainUrl = raw_input("Enter the main Url: ")

#Create a Fetcher object
myFetcher = Fetcher()

#Create an Injection object

myInjection = Injection()

#Create a Parser object
myParser = Parser()
yesList = ["yes","Yes","YES","y","Y","YEs","YeS","yEs","yeS"]

noList = ["no","No","n","N","nO","NO"]

def tryAgain():
	loginUrl = raw_input("URL Invalid. Try again: ")
	try:
        	myFetcher.login(loginUrl)
        except:
                tryAgain()


def checkLogin():

	isLogin = raw_input("Is there a login page? {yes/no}: ")

	if isLogin in yesList:
		loginUrl = raw_input("What is the login URL?: ")
		#success = false
		#while success != true: 
			#Run the login
		try:
			myFetcher.login(loginUrl)
		except:
			tryAgain()
	
		#Set cookies
                myInjection.setCookies(myFetcher.getCookies())

                #Set target URL
                myInjection.setURL(myFetcher.getUrlWithRequest())

	elif isLogin in noList:
		#Set cookies
		myInjection.setCookies(myFetcher.getCookies())

		#Set target URL
		myInjection.setURL(myFetcher.getUrlWithRequest())
	else:
		print "Invalid entry"
		checkLogin()
#Run the full injection method
checkLogin()
myInjection.fullInject()

#Run the parser methods
#myParser.dbsParse("dbsList.txt")
#myParser.tblParse("tableList.txt")
