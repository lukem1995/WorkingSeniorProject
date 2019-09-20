#References https://www.pythonforbeginners.com/cheatsheet/python-mechanize-cheat-sheet

import mechanize
import cookielib
import time

class HTMLGetter():

	def __init__(self):
		self.browser = mechanize.Browser()
                self.cookiejar = cookielib.CookieJar()
                self.browser.set_cookiejar(self.cookiejar)
                self.browser.set_handle_robots(False)
		self.fileName = "myHTML.html"
		self.domain = None
		self.password = "None"
		self.username = "None"

	def setCredentials(self, username, password):
		self.username = username
		self.password = password

	def login(self):
		try:
			pageBefore = self.browser.open(self.domain)
			self.browser.select_form(nr=0)
			self.browser["username"] = self.username
			self.browser["password"] = self.password
			self.browser.submit()
			pageAfter = self.browser.open(self.domain)
			if pageBefore == pageAfter:
				print "Login failed. Try again"
				exit()
			print "Login successful"
		except:
			print "Login failed. Try again"
			exit()

	def getHTML(self, url):
		self.domain = url
		try:
			html = self.browser.open(url)
			with open(self.fileName,"w+") as htmlFile:
				htmlFile.write(html.read())
				htmlFile.close()
		except:
			None
		#time.sleep(5)
	def getFileName(self):
		return self.fileName
