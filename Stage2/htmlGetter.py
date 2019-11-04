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

	def login2(self,url):
		try:
			count = 0
			count2 = 0
			self.browser.open(url)
			for form in self.browser.forms():
				self.browser.form = list(self.browser.forms())[count]
				for control in self.browser.form.controls:
					if control.type == "submit":
						control.disabled = True
				for control in self.browser.form.controls:
					inputname = str(control.name)
					self.browser.select_form(nr=count)
					if not control.disabled:
						if count2 == 0:
							self.browser[inputname] = self.username
						elif count2 == 1:
							self.browser[inputname] = self.password
						count2 = count2 + 1
				self.browser.submit()
				count = count + 1
				print "Login successful"
		except:
			print "Login failed"
			exit()

	def login(self,url):
		try:
			self.domain = url
			pageBefore = self.browser.open(self.domain)
			self.browser.select_form(nr=0)
			self.browser["username"] = self.username
			self.browser["password"] = self.password
			for control in self.browser.form.controls:
				print self.browser[control.name]
			self.browser.submit()
			pageAfter = self.browser.open(self.domain)
			with open("loginHTML.html","w+") as loginHTML:
				loginHTML.write(pageAfter.read())
				loginHTML.close()
			if pageBefore == pageAfter:
				print "Login failed 1. Try again"
				exit()
			print "Login successful"
		except:
			print "Login failed 2. Try again"
			exit(1)

	def getHTML(self, url):
		self.domain = url
		if "logout" not in str(url):
			try:
				html = self.browser.open(url)
				print self.browser.geturl()
				with open(self.fileName,"w+") as htmlFile:
					htmlFile.write(html.read())
					htmlFile.close()
			except:
				None
			#time.sleep(5)
	def getFileName(self):
		return self.fileName

	def xss(self, url, myPayload):
		payload = myPayload
		vulnerable = False
		print "working on " + str(url)
		pcount = 0
		for i in payload:
			try:
				self.browser.open(url)
				# print self.browser.geturl()
				count = 0
				for form in self.browser.forms():
					# print "Form ", count + 1
					self.browser.form = list(self.browser.forms())[count]
					for control in self.browser.form.controls:
						if control.type == "submit":
							control.disabled = True
					for control in self.browser.form.controls:
						inputname = str(control.name)
						self.browser.select_form(nr=count)
						if not control.disabled:
							self.browser[inputname] = str(payload[pcount])
					self.browser.submit()
					fullUrl = self.browser.geturl()
					#fullUrl = fullUrl + "&Submit=Submit"
					#print fullUrl
					response = self.browser.open(fullUrl)
					if str(payload[pcount]) in str(response.read()):
						vulnerable = True
					# with open("attack_response.html", "w+") as htmlFile:
					#	htmlFile.write(response.read())
					#	htmlFile.close()
					count = count + 1
			except:
				#print "Form failed"
				None
			pcount = pcount + 1
		return vulnerable

	def sql(self, url, myPayload):
		payload = myPayload
		vulnerable = False
		print "working on " + str(url)
		pcount = 0
		for i in payload:
			try:
				self.browser.open(url)
				#print self.browser.geturl()
				count = 0
				for form in self.browser.forms():
					#print "Form ", count + 1
					self.browser.form = list(self.browser.forms())[count]
					for control in self.browser.form.controls:
						if control.type == "submit":
							control.disabled = True
					for control in self.browser.form.controls:
						inputname = str(control.name)
						self.browser.select_form(nr=count)
						if not control.disabled:
							self.browser[inputname] = str(payload[pcount])
					self.browser.submit()
					fullUrl = self.browser.geturl()
					fullUrl = fullUrl + "&Submit=Submit"
					response = self.browser.open(fullUrl)
					#print str(fullUrl)
					#print str(response.read())
					if "SQL syntax" in str(response.read()):
						vulnerable = True
					#print fullUrl
					#response = self.browser.open(fullUrl)
					#with open("attack_response.html", "w+") as htmlFile:
					#	htmlFile.write(response.read())
					#	htmlFile.close()
					count = count + 1
			except:
				print "Form failed"
			pcount = pcount + 1
		return vulnerable
