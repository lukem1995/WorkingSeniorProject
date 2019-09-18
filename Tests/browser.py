#Referenced https://stackoverflow.com/questions/21190395/python-mechanize-login/21190761 and Violent Python

import mechanize
import cookielib
import xml

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

	#Returns Cookies
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

	#Open browser session
	def openDomain(self):
		try:
			self.domainSession = self.browser.open(self.fullDomain)
		except:
			print self.fullDomain
			print "Bad domain. Try again"
			self.setDomain()

        #Get target domain from user
        def setDomain(self):
                self.fullDomain = raw_input("Enter the desired domain: ")
		if self.fullDomain.startswith("http://") or self.fullDomain.startswith("https://"):
			self.openDomain()
		else:
			self.fullDomain = "http://" + self.fullDomain
			self.openDomain()

	#Returns the domain being used
	def getDomainName(self):
		return self.fullDomain

	#Checks for sitemap on chosen domain and if present writes to file
	def checkSitemap(self):		
		self.siteMapUrl = self.fullDomain + "/sitemap"
		try:
			self.domainSession = self.browser.open(self.siteMapUrl)
			mySitemap = self.domainSession.read()
			with open(self.sitemapFile,"w+") as sitemap:
				siteMap.write(mySitemap)
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
                		#print "Saved HTML to " + self.htmlFile
				return False
	
	def checkLink(self,url):
		#print url
		try:
			#print url
			self.browser.open(url,timeout=4)
			return True
		except:
			return False
