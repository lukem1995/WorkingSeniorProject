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

	def login(self, url):
		print url
		print self.username
		print self.password
		try:
			self.domain = url
			self.browser.open(self.domain)
			self.browser.select_form(nr=0)
			self.browser["username"] = self.username
			self.browser["password"] = self.password
			#self.browser["Login"] = "login"
			self.browser.submit()
			print "Login successful"
		except:
			print "Login failed 2. Try again"
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

	def getForms(self, url):
		self.domain = url
		self.browser.open(url)
		for form in self.browser.forms():
			print "Form name: ", form.name

# Method taken almost directly from https://www.pythonforbeginners.com/cheatsheet/python-mechanize-cheat-sheet
	def mechforms(self, url):
		self.browser.open(url)
		count = 0
		for form in self.browser.forms():
			print "Form ", count + 1
			#print "Form name: ", form.name
			#print form
			self.browser.form = list(self.browser.forms())[count]
			for control in self.browser.form.controls:
				if control.type == "submit":
					control.disabled = True
			for control in self.browser.form.controls:
				#print control
				#print "type=%s, name=%s value=%s" % (control.type, control.name, self.browser[control.name])
				if control.type == "text":  # means it's class ClientForm.TextControl
					control.value = "\'SELECT * FROM Users WHERE UserId = 105 OR 1=1;\'"
					print "input"
			response = self.browser.submit()
			print response.read()
			#self.browser.back()
			count = count + 1
