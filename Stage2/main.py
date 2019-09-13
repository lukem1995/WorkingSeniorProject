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
myDomain = None

#Gets domain from user and sets it to a variable
myBrowser.setDomain()
myDomain = myBrowser.getDomain()

#Checks for sitemap
#If sitemap found, gets links from <loc> tags and saves to list
#If sitemap not found, gets HTML from domain index and saves to file 
if myBrowser.checkSitemap() == True:
	myXmlParser.setFile(myBrowser.sitemapFile)
	myXmlParser.setLinks()
	links = myXmlParser.getLinks()
	if len(links) == 0:
		print "Sitemap is in a bad format"
else:
	myHtmlGetter.getHTML(myDomain)


#Prints all links in the links list
def showLinks():
	count = 0
	for i in links:
		print links[count]
		count = count + 1
		#print type(count)


#Attempts to reach the links in the links list and adds them to a list of good links if they're reachable
def checkLinks():
	count = 0
	with open("GoodLinks.txt","w+") as glFile:
		glFile.close()
		for i in links:
			if myBrowser.checkLink(links[count]) == True:
				with open("GoodLinks.txt","a") as glFile:
					glFile.write(links[count] + "\n")
					glFile.close()
				goodLinks.append(links[count])
				print links[count] + " is good" 
				print str(count + 1) +  "/" + str(len(links) + 1)
			else:
				print links[count] + " is bad"
				print str(count + 1) + "/" + str(len(links) + 1)
			count = count + 1

showLinks()
checkLinks()
#print len(links)
#print myBrowser.fullDomain
