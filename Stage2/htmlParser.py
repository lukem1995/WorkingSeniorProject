from bs4 import BeautifulSoup

class HTMLParser():
	def __init__(self,htmlFile):
		self.file = htmlFile
		self.soup = BeautifulSoup(self.file,"html.parser")
		#print self.soup.title.string

	def getLinks(self):
		for link in self.soup.findAll("a"):
			print link.get("href")
