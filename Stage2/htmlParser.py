from bs4 import BeautifulSoup

class HTMLParser():
	def __init__(self):
		self.file = None
		self.soup = None
		self.links = []

	def setFile(self,htmlFile):
		self.file = htmlFile
                self.soup = BeautifulSoup(self.file,"html.parser")

	def setLinks(self):
		count = 0
		for url in self.soup.findAll("a"):
			link = url.get("href")
			self.links.append(link)
	def getLinks(self): 
		return self.links
