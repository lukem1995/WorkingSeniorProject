import time
import sys
reload(sys)
sys.setdefaultencoding("utf8")
sys.setrecursionlimit(1000000)
from browser import Browser
from xmlParser import XmlParser
from htmlGetter import HTMLGetter
from htmlParser import HTMLParser


#Modified from code at https://thispointer.com/python-how-to-replace-single-or-multiple-characters-in-a-string/
        #(Change is that mine works on a list of strings instead of just one string)
#Removes list of strings from list of strings, modyfying the list
def replaceMultipleList(mainStringList, newString):
	toReplace = ["https://","http://","www."]
	count = 0
	for i in mainStringList:
		for j in toReplace:
			if str(j) in str(i):
				mainStringList[count] = mainStringList[count].replace(j, newString)
		count = count + 1
	return mainStringList

#Copied from https://thispointer.com/python-how-to-replace-single-or-multiple-characters-in-a-string/
#Removes list of strings from string
def replaceMultiple(mainString, newString):
	toReplace = ["https://","http://","www."]
	count = 0
	for elem in toReplace:
		if elem in mainString:
 			mainString = mainString.replace(elem, newString)
	return mainString


#Gets domain from user and sets varaibles
def start():
	global myBrowser
	myBrowser.setDomain()
	domainName = myBrowser.getDomainName()
	shortDomainName = replaceMultiple(domainName,"")
	return domainName, shortDomainName;

def isSitemap(myDomain):
	global myBrowser
	global myXmlParser
	myLinks = None
#Checks for sitemap
#If sitemap found, gets links from <loc> tags and saves to list
#If sitemap not found, gets HTML from domain index and saves to file 
	if myBrowser.checkSitemap() == True:
		myXmlParser.setFile(myBrowser.sitemapFile)
		myXmlParser.setLinks()
		myLinks = myXmlParser.getLinks()
		#Runs if sitemap exists but parsing returns no links
		if len(myLinks) == 0:
			print("Sitemap is in a bad format")
			myLinks = noSitemap(myDomain,myDomain)
			return myLinks;
		return myLinks;
	#Runs if no sitemap found
	else:
		myLinks = noSitemap(myDomain,myDomain)
		return myLinks;

def noSitemap(myPage,myDomain):
	global recursiveLinks
	returnedLinks = scrapePage(myPage)
	#showLinks(returnedLinks)
	returnedLinks = cleanLinks(returnedLinks,myDomain)
	returnedLinks = isDomain(returnedLinks,myDomain)
	returnedLinks = rmDup(returnedLinks)

	pageCount = 0
	for i in returnedLinks:
		if str(returnedLinks[pageCount]) not in recursiveLinks:
			print str(returnedLinks[pageCount])
			recursiveLinks.append(str(returnedLinks[pageCount]))
			noSitemap(str(returnedLinks[pageCount]),myDomain)
		pageCount = pageCount + 1

	showLinks(recursiveLinks)
	return recursiveLinks

def scrapePage(myPage):
	global myHtmlGetter
	global myHtmlParser
	myLinks = 0

	myHtmlGetter.getHTML(myPage)
        with open(myHtmlGetter.getFileName(), "r") as file:
        	myHtmlFile = file.read()
        	file.close()
        myHtmlParser.setFile(myHtmlFile)
        myHtmlParser.setLinks()
        myLinks = myHtmlParser.getLinks()
	return myLinks

#Prints all links in the links list
def showLinks(myLinks):
	for i in myLinks:
		print str(i)

def isDomain(myLinks,myDomain):
	matchedLinks = []
	#myLinks = replaceMultipleList(myLinks,"")
	for i in myLinks:
		if str(i).startswith(myDomain):
			matchedLinks.append(str(i))
	return matchedLinks

def cleanLinks(myLinks,myDomain):
	count = 0
	for i in myLinks:
		try:
			if str(myLinks[count])[0] == "/":
				myLinks[count] = str(myDomain) + str(myLinks[count])

			elif str(myLinks[count]) == "#":
				myLinks[count] = str(myDomain)
		except:
			None
		count = count + 1
	myLinks = replaceMultipleList(myLinks,"")
	count = 0
	for i in myLinks:
		myLinks[count] = "http://" + str(myLinks[count])
		count = count + 1
	return myLinks

#From https://www.w3schools.com/python/python_howto_remove_duplicates.asp
#Removes dupicates from list
def rmDup(myList):
	myList = list(dict.fromkeys(myList))
	return myList

#Attempts to reach the links in the links list and adds them to a list of good links if they're reachable
def checkLinks(myLinks):
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
	return goodLinks

#Main
def main():
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

	myDomainName = None
	shortDomain = None
	sitemapBool = None
	matchedDomains = []
	validLinks = []
	links = []

	myDomainName, shortDomain = start()
	links = isSitemap(myDomainName)

	links = cleanLinks(links,myDomainName)
	matchedDomains = isDomain(links,myDomainName)
	matchedDomains = rmDup(matchedDomains)
	validLinks = checkLinks(matchedDomains)

if __name__ == "__main__":
	main()
