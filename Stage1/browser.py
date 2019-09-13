#Referenced https://stackoverflow.com/questions/21190395/python-mechanize-login/21190761 and Violent Python
import mechanize
import cookielib

def viewPage(myUrl):
	browser = mechanize.Browser()
	cookiejar = cookielib.CookieJar()
	browser.set_cookiejar(cookiejar)
	browser.set_handle_robots(False)
	page = browser.open(myUrl)
	browser.select_form(nr=0)
	browser["username"] = 'Admin'
	browser["password"] = 'password'
	browser.submit()
	#source_code = page.read()
	#print source_code
	#print browser.select_form(nr=0)
	url = browser.open("http://10.0.2.4/vulnerabilities/sqli")
	browser.select_form(nr=0)
	browser["id"] = "1"
	browser.submit()
	jackpot = browser.geturl()
	print jackpot
	count = 0
	for cookie in cookiejar:
		count = count+1
		print cookie.name, cookie.value
	
	#print cookiejar.extract_cookies()
viewPage('http://10.0.2.4')
