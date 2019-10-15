#Referenced https://stackoverflow.com/questions/21190395/python-mechanize-login/21190761 and Violent Python

import mechanize
import cookielib
import xml


# noinspection PyInconsistentIndentation
class Browser():

	def __init__(self):
		self.browser = mechanize.Browser()
                self.cookiejar = cookielib.CookieJar()
                self.browser.set_cookiejar(self.cookiejar)
                self.browser.set_handle_robots(False)
		self.domain = None
		self.fullDomain = None
		self.siteMapUrl = None
		self.domainSession = None
		self.sitemapFile = "mySitemap.xml"
		self.htmlFile = "myHTML.html"
		self.username = "None"
		self.password = "None"

	# Returns Cookies
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

	# Sets credentials
	def setCredentials(self, username, password):
		self.username = username
		self.password = password

	# Log into site
	def login(self, url):
		try:
			pageBefore = self.browser.open(url)
			self.browser.select_form(nr=0)
			self.browser["username"] = self.username
			self.browser["password"] = self.password
			self.browser.submit()
			pageAfter = self.browser.open(self.fullDomain)
			if pageBefore == pageAfter:
				print "Login failed. Try again"
				exit()
			print "Login successful"
		except:
			print "Login failed. Try again"
			exit()

	# Open browser session
	def openDomain(self):
		try:
			self.domainSession = self.browser.open(self.fullDomain)
		except:
			print self.fullDomain
			print "Bad domain. Try again"
			self.setDomain()

    # Get target domain from user
	def setDomain(self):
		self.fullDomain = raw_input("Enter the desired domain: ")
		if self.fullDomain.startswith("http://") or self.fullDomain.startswith("https://"):
			self.openDomain()
		else:
			self.fullDomain = "http://" + self.fullDomain
			self.openDomain()

	# Returns the domain being used
	def getDomainName(self):
		return self.fullDomain

	# Checks for sitemap on chosen domain and if present writes to file
	def checkSitemap(self):		
		self.siteMapUrl = self.fullDomain + "/sitemap"
		try:
			self.domainSession = self.browser.open(self.siteMapUrl)
			mySitemap = self.domainSession.read()
			with open(self.sitemapFile,"w+") as sitemap:
				sitemap.write(mySitemap)
				return True

		except:
			self.siteMapUrl = self.fullDomain + "/sitemap.xml"
			try:
				self.domainSession = self.browser.open(self.siteMapUrl)
				mySitemap = self.domainSession.read()
				with open(self.sitemapFile,"w+") as siteMap:
					siteMap.write(mySitemap)
					return True
			except:
                		with open(self.htmlFile,"w+") as htmlFile:
                        		htmlFile.write(self.domainSession.read())
                        		htmlFile.close()
				print "No sitemap found"
                		# print "Saved HTML to " + self.htmlFile
				return False
	
	def checkLink(self,url):
		# print url
		if "logout" not in str(url):
			try:
				# print url
				self.browser.open(url, timeout=4)
				print self.browser.geturl()
				return True
			except:
				return False
