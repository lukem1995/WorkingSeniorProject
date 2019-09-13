from bs4 import BeautifulSoup

class HTMLParser():
	def __init__(self):
		self.file = None
		self.soup = None
		#print self.soup.title.string

	def setFile(self,htmlFile):
		self.file = htmlFile
                self.soup = BeautifulSoup(self.file,"html.parser")

	def getLinks(self):
		for link in self.soup.findAll("a"):
			print link.get("href")
		print "Done"
