from bs4 import BeautifulSoup


# noinspection PyComparisonWithNone
class HTMLParser():
	def __init__(self):
		self.file = None
		self.soup = None
		self.links = []
		self.forms = {}
		self.formType = "None"

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

	def setForms(self):
		count = 0
		for url in self.soup.findAll("input"):
			formName = url.get("name")
			if formName is not None:
				self.forms.update({str(count): str(formName)})
			count = count + 1

	def getForms(self):
		return self.forms

	def setFormMethod(self):
		for url in self.soup.findAll("form"):
			self.formType = url.get("method")
			print self.formType

	def getFormMethod(self):
		print self.formType
		return str(self.formType)



