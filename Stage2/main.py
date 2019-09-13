import time
from browser import Browser
from xmlParser import XmlParser
from htmlGetter import HTMLGetter
from htmlParser import HTMLParser


myBrowser = Browser()
myXmlParser = XmlParser()
myHtmlGetter = HTMLGetter()
myHtmlParser = HTMLParser()
xmlFile = None
goodLinks = []
links = None
myDomainName = None
myHtmlFile = None

#Gets domain from user and sets it to a variable
myBrowser.setDomain()
myDomainName = myBrowser.getDomainName()

#Checks for sitemap
#If sitemap found, gets links from <loc> tags and saves to list
#If sitemap not found, gets HTML from domain index and saves to file 
if myBrowser.checkSitemap() == True:
	myXmlParser.setFile(myBrowser.sitemapFile)
	myXmlParser.setLinks()
	links = myXmlParser.getLinks()
	#Runs if sitemap exists but parsing returns no links
	if len(links) == 0:
		print "Sitemap is in a bad format"
		myDomain = myHtmlGetter.getHTML(myDomain)
        	with open(myHtmlGetter.getFileName(), "r") as file:
                	myHtmlFile = file.read()
                	file.close()
        	myHtmlParser.setFile(myHtmlFile)
        	myHtmlParser.setLinks()
        	links = myHtmlParser.getLinks()
#Runs if no sitemap found
else:
	myHtmlGetter.getHTML(myDomainName)
	with open(myHtmlGetter.getFileName(), "r") as file:
        	myHtmlFile = file.read()
        	file.close()
	myHtmlParser.setFile(myHtmlFile)
	myHtmlParser.setLinks()
	links = myHtmlParser.getLinks()

#Prints all links in the links list
def showLinks():
	count = 0
	for i in links:
		print str(links[count])
		count = count + 1
		#print type(count)

def cleanLinks():
	count = 0
	for i in links:
		print str(links[count])[0]
		if str(links[count])[0] == "/":
			links[count] = str(myDomainName) + str(links[count])
			print links[count]

		elif str(links[count]) == "#":
			links[count] = str(myDomainName)
			print links[count]
		else:
			print str(links[count])
		count = count + 1

#Attempts to reach the links in the links list and adds them to a list of good links if they're reachable
def checkLinks():
	count = 0
	with open("GoodLinks.txt","w+") as glFile:
		glFile.close()
		for i in links:
			if myBrowser.checkLink(links[count]) == True:
				if links[count] in goodLinks:
					print str(links[count]) + " is a duplicate"
                                	print str(count + 1) +  "/" + str(len(links))

				else:
					with open("GoodLinks.txt","a") as glFile:
                                        	glFile.write(links[count] + "\n")
                                        	glFile.close()
					goodLinks.append(links[count])
					print str(links[count]) + " is good" 
					print str(count + 1) +  "/" + str(len(links))
			else:
				print str(links[count]) + " is bad"
				print str(count + 1) + "/" + str(len(links))
			count = count + 1
			time.sleep(1)

#showLinks()
cleanLinks()
checkLinks()
#print len(links)
#print myBrowser.fullDomain
