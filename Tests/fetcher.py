#Referenced https://stackoverflow.com/questions/21190395/python-mechanize-login/21190761 and Violent Python
import mechanize
import cookielib

class Fetcher():
	
	def __init__(self):
		self.browser = mechanize.Browser()
		self.cookiejar = cookielib.CookieJar()
		self.browser.set_cookiejar(self.cookiejar)
		self.browser.set_handle_robots(False)
		self.username = ""
		self.password = ""

	def setCredentials(self, username, password):
		self.username = username
		self.password = password

	def login(self,myUrl):
		#username = raw_input("Enter the username: ")
		#password = raw_input("Enter your password: ")
		try:
			page = self.browser.open(myUrl)
			self.browser.select_form(nr=0)
			print self.username,", ",self.password
			self.browser["username"] = self.username
			self.browser["password"] = self.password
			self.browser.submit()
			print "Login successful"
		except:
			print "Login unsuccessful"

	def getUrlWithRequest(self):
		attackUrl = raw_input("Enter the attack url: ")
		self.browser.open(attackUrl)
		fullUrl = self.browser.geturl()
		print fullUrl
		#self.browser.select_form(nr=0)
		#self.browser["id"] = "1"
		#self.browser.submit()
		#fullUrl = self.browser.geturl()
		#return fullUrl

	def getCookies(self):
		count = 0
		for cookie in self.cookiejar:
			cookiename = cookie.name
			cookievalue = cookie.value
			if count == 0: 
				fullcookies = cookiename + "=" + cookievalue
			else: 
				fullcookies = fullcookies + ";" + cookiename + "=" + cookievalue
			count = count + 1
		return fullcookies
