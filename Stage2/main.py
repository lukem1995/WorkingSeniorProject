from browser import Browser
from xmlParser import XmlParser

myBrowser = Browser()
myParser = XmlParser()
xmlFile = None
goodLinks = []
links = None

myBrowser.setDomain()


if myBrowser.checkSitemap() == True:
	myParser.setFile(myBrowser.sitemapFile)
	myParser.setLinks()
	links = myParser.getLinks()
	if len(links) == 0:
		print "Sitemap is in a bad format. Exiting"
else:
	print "exit"
	exit()

def showLinks():
	count = 0
	for i in links:
		print links[count]
		count = count + 1
		#print type(count)
showLinks()

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
checkLinks()
#print len(links)
#print myBrowser.fullDomain
