import mechanize
import cookielib
from bs4 import BeautifulSoup

class FormTest:
	def __init__(self):
		self.browser = mechanize.Browser()
                self.cookiejar = cookielib.CookieJar()
                self.browser.set_cookiejar(self.cookiejar)
                self.browser.set_handle_robots(False)
	def getHTML(self, url):
		myPage = self.browser.open(url)
		myHTML = open("html.txt","w+")
		myHTML.write(myPage.read())
		#soup = BeautifulSoup(myHTML,"lxml")
		#prettyHTML = open("prettyHTML.html","w+")
		#prettyHTML.write(soup.prettify())
		soup = BeautifulSoup("html","html.parser")
                print soup.body.div.findall("form")
		print "Success!"
myTest = FormTest()
myTest.getHTML("http://10.0.2.4")
