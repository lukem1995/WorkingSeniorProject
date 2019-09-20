import time
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import getopt
from browser import Browser
from xmlParser import XmlParser
from htmlGetter import HTMLGetter
from htmlParser import HTMLParser


# Modified from code at https://thispointer.com/python-how-to-replace-single-or-multiple-characters-in-a-string/
        # (Change is that mine works on a list of strings instead of just one string)
# Removes list of strings from list of strings, modyfying the list
def replaceMultipleList(mainStringList, newString):
	toReplace = ["https://","http://","www."]
	count = 0
	for i in mainStringList:
		for j in toReplace:
			if str(j) in str(i):
				mainStringList[count] = mainStringList[count].replace(j, newString)
		count = count + 1
	return mainStringList

# Copied from https://thispointer.com/python-how-to-replace-single-or-multiple-characters-in-a-string/
# Removes list of strings from string
def replaceMultiple(mainString, newString):
	toReplace = ["https://","http://","www."]
	count = 0
	for elem in toReplace:
		if elem in mainString:
			mainString = mainString.replace(elem, newString)
	return mainString


# Gets domain from user and sets varaibles
def start():
	global myBrowser
	myBrowser.setDomain()
	domainName = myBrowser.getDomainName()
	shortDomainName = replaceMultiple(domainName,"")
	return domainName, shortDomainName;

def isSitemap(myDomain):
	global myBrowser
	global myXmlParser
	myLinks = []
	myDomainList = []
# Checks for sitemap
# If sitemap found, gets links from <loc> tags and saves to list
# If sitemap not found, gets HTML from domain index and saves to file
	if myBrowser.checkSitemap() == True:
		myXmlParser.setFile(myBrowser.sitemapFile)
		myXmlParser.setLinks()
		myLinks = myXmlParser.getLinks()
		# Runs if sitemap exists but parsing returns no links
		if len(myLinks) == 0:
			print("Sitemap is in a bad format")
			myDomainList = scrapePage(myDomain)
			myLinks = noSitemap(myDomainList,myDomain)
			return myLinks;
		return myLinks;
	# Runs if no sitemap found
	else:
		#print myDomain
		#print type(myDomain)
		myDomainList = scrapePage(myDomain)
		#showLinks(myDomainList)
		#print myDomain
		myLinks = noSitemap(myDomainList,myDomain)
		return myLinks;

# ecursively finds pages
def noSitemap(myPageList,myDomain):
	global recursiveLinks
	global recursionCount
	nextList = []
	currentList = []
	myLinks = []
	print recursionCount
	#returnedLinks = scrapePage(myPage)
	#showLinks(returnedLinks)
	myPageList = rmDup(myPageList)
	myPageList = cleanLinks(myPageList,myDomain)
	myPageList = isDomain(myPageList,myDomain)
	myPageList = rmDup(myPageList)

	pageCount = 0
	for i in myPageList:
		if str(myPageList[pageCount]) not in recursiveLinks:
			print str(myPageList[pageCount])
			recursiveLinks.append(str(myPageList[pageCount]))
			currentList = scrapePage(str(myPageList[pageCount]))
			currentCount = 0
			for j in currentList:
				nextList.append(str(currentList[currentCount]))
				currentCount = currentCount + 1
			#nextList.append(str(returnedLinks[pageCount]),myDomain)
		print recursionCount + 1, ",", pageCount, "/", len(myPageList)
		pageCount = pageCount + 1
	
	if len(nextList) == 0:
		#showLinks(recursiveLinks)
		myPageList = recursiveLinks
		#showLinks(myPageList)
		#print "here"
		return myPageList
	else:
		recursionCount = recursionCount + 1
		noSitemap(nextList,myDomain)

# Gets links from given page
def scrapePage(myPage):
	global myHtmlGetter
	global myHtmlParser
	myLinks = []

	myHtmlGetter.getHTML(myPage)
        with open(myHtmlGetter.getFileName(), "r") as file:
        	myHtmlFile = file.read()
        	file.close()
        myHtmlParser.setFile(myHtmlFile)
        myHtmlParser.setLinks()
    	myLinks = myHtmlParser.getLinks()
	return myLinks

# Prints all links in the links list
def showLinks(myLinks):
	for i in myLinks:
		print str(i)

def isDomain(myLinks,myDomain):
	print "begin domain check"
	matchedLinks = []
	#myLinks = replaceMultipleList(myLinks,"")
	count = 0
	count2 = 1
	for i in myLinks:
		if str(i).startswith(myDomain):
			matchedLinks.append(str(i))
			count = count + 1 
		print "Domain check: ", count2, "/", len(myLinks)
		count2 = count2 + 1
	print "end domain check"
	return matchedLinks

def cleanLinks(myLinks,myDomain):
	count = 0
	print "begin clean"
	try:
		for i in myLinks:
			try:
				if str(myLinks[count])[0] == "/":
					myLinks[count] = str(myDomain) + str(myLinks[count])

				elif str(myLinks[count]) == "#":
					myLinks[count] = str(myDomain)

				elif str(myLinks[count]) == "None" or str(myLinks[count]) == "none":
					myLinks.pop(count)
			except:
				None
			print "Cleaning: ", count + 1, "/" , len(myLinks)
			count = count + 1
		myLinks = replaceMultipleList(myLinks,"")
		myLinks = rmDup(myLinks)
		count = 0
		for i in myLinks:
			myLinks[count] = "http://" + str(myLinks[count])
			print "Cleaning part2: ", count + 1, "/", len(myLinks)
			count = count + 1
		print "end clean"	
		return myLinks
	except:
		print "could not clean"
		return myLinks

# From https://www.w3schools.com/python/python_howto_remove_duplicates.asp
# Removes dupicates from list
def rmDup(myList):
	print "begin rmDup"
	myList = list(dict.fromkeys(myList))
	print "end rmdup"
	return myList

# Attempts to reach the links in the links list and adds them to a list of good links if they're reachable
def checkLinks(myLinks):
	print "Begin validation"
	global myBrowser
	count = 0
	goodLinks = []
	with open("GoodLinks.txt","w+") as glFile:
		glFile.close()
	for i in myLinks:
		if myBrowser.checkLink(i) == True:
			with open("GoodLinks.txt","a") as glFile:
                        	glFile.write(i + "\n")
                        	glFile.close()
			goodLinks.append(i)
			print str(i) + " is good" 
			print str(count + 1) +  "/" + str(len(myLinks))
		else:
			print str(i) + " is bad"
			print str(count + 1) + "/" + str(len(myLinks))
		count = count + 1
		#time.sleep(2)
	print "End validation"
	return goodLinks

# Main
def main(argv):
	global myBrowser
	myBrowser = Browser()
	global myXmlParser
	myXmlParser = XmlParser()
	global myHtmlGetter
	myHtmlGetter = HTMLGetter()
	global myHtmlParser
	myHtmlParser = HTMLParser()

	global recursiveLinks
	recursiveLinks = []
	global recursionCount
	recursionCount = 1

	isLogin = False
	myUsername = "None"
	myPassword = "None"
	myDomainName = "None"
	shortDomain = "None"
	sitemapBool = None
	matchedDomains = []
	validLinks = []
	links = []

	try:
		opts, args = getopt.getopt(argv, "u:p:d:", ["login", "domain="])
	except getopt.GetoptError:
		print "(optional)\n--login followed by \n -u <username> -p <password> "
		exit()

	for opt, arg in opts:
		if opt == "--login":
			isLogin = True
		elif opt == "-u":
			myUsername = arg
		elif opt == "-p":
			myPassword = arg

	if isLogin:
		myBrowser.setCredentials(myUsername, myPassword)
		myDomainName, shortDomain = start()
		myBrowser.login()
		myHtmlGetter.getHTML(myDomainName)
		exit()
	else:
		myDomainName, shortDomain = start()

	isSitemap(myDomainName)
	#showLinks(recursiveLinks)
	#print recursiveLinks
	#cleanLinks(recursiveLinks,myDomainName)
	#matchedDomains = isDomain(links,myDomainName)
    #matchedDomains = rmDup(matchedDomains)
	validLinks = checkLinks(recursiveLinks)

if __name__ == "__main__":
	main(sys.argv[1:])
