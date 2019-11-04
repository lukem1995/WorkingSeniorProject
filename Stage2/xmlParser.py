#Referenced https://docs.python.org/2/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET

class XmlParser():
	def __init__(self):
		self.tree = None
		self.root = None
                self.xmlns = None
		self.links = []

	def setFile(self,file):
		self.tree = ET.parse(file)
		self.root = self.tree.getroot()
		 # From https://stackoverflow.com/questions/9513540/python-elementtree-get-the-namespace-string-of-an-element
                self.xmlns = self.root.tag.split("}")[0].strip("{")
                ####
		self.nsmap = {'sites':self.xmlns}


	def setLinks(self):
		#count = 0
		#From https://stackoverflow.com/questions/44967802/get-values-from-child-nodes-from-xml-python
		for url in self.root.findall('sites:url',self.nsmap):
			link = url.find('sites:loc',self.nsmap).text
			self.links.append(link)
			#print self.links[count]
			#count = count +1

	def getLinks(self):
		return self.links
