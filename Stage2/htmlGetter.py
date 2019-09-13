#References https://www.pythonforbeginners.com/cheatsheet/python-mechanize-cheat-sheet

import mechanize
import cookielib

class HTMLGetter():

	def __init__(self):
		self.browser = mechanize.Browser()
                self.cookiejar = cookielib.CookieJar()
                self.browser.set_cookiejar(self.cookiejar)
                self.browser.set_handle_robots(False)
		self.fileName = "myHTML.html"
		self.domain = None

	def getHTML(self, url):
		self.domain = url
		html = self.browser.open(url)
		with open(self.fileName,"w+") as htmlFile:
			htmlFile.write(html.read())
			htmlFile.close()
		print "Saved HTML to " + self.fileName

	def getFileName(self):
		return self.fileName
