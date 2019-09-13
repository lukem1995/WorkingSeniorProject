#Referenced https://stackoverflow.com/questions/21190395/python-mechanize-login/21190761 and Violent Python
import mechanize
import cookielib

class Fetcher():
	
	def __init__(self):
		self.browser = mechanize.Browser()
                self.cookiejar = cookielib.CookieJar()
               	self.browser.set_cookiejar(self.cookiejar)
                self.browser.set_handle_robots(False)

	def login(self,myUrl):
		username = raw_input("Enter the username: ")
		password = raw_input("Enter your password: ")
		page = self.browser.open(myUrl)
		self.browser.select_form(nr=0)
		self.browser["username"] = username
		self.browser["password"] = password
		self.browser.submit()
		#print "login successful"
	def getUrlWithRequest(self):
		attackUrl = raw_input("Enter the attack url: ")
		url = self.browser.open(attackUrl)
		self.browser.select_form(nr=0)
		self.browser["id"] = "1"
		self.browser.submit()
		fullUrl = self.browser.geturl()
		return fullUrl

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
