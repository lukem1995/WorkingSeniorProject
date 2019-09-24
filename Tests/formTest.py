import sys
import getopt
from browser import Browser
from htmlGetter import HTMLGetter
from htmlParser import HTMLParser
#sys.setdefaultencoding("utf8")

# Copied from https://thispointer.com/python-how-to-replace-single-or-multiple-characters-in-a-string/
# Removes list of strings from string
def replaceMultiple(mainString, newString):
    toReplace = ["https://", "http://", "www."]
    for elem in toReplace:
        if elem in mainString:
            mainString = mainString.replace(elem, newString)
    return mainString

def start():
    global myBrowser
    myBrowser.setDomain()
    domainName = myBrowser.getDomainName()
    #shortDomainName = replaceMultiple(domainName,"")
    return domainName

def scrapePage(myPage):
    global myHtmlGetter
    global myHtmlParser
    global myForms
    global formType

    myHtmlGetter.getHTML(myPage)
    with open(myHtmlGetter.getFileName(), "r") as file:
        myHtmlFile = file.read()
        file.close()
    myHtmlParser.setFile(myHtmlFile)
    myHtmlParser.setForms()
    myForms = myHtmlParser.getForms()
    myHtmlParser.setFormMethod()
    formType = myHtmlParser.getFormMethod

def main(argv):
    global myBrowser
    myBrowser = Browser()
    global myHtmlGetter
    myHtmlGetter = HTMLGetter()
    global myHtmlParser
    myHtmlParser = HTMLParser()
    global formType
    formType = "None"

    isLogin = False
    myUsername = "None"
    myPassword = "None"
    attackURL = "None"

    global myForms
    myForms = {}

    try:
        opts, args = getopt.getopt(argv, "u:p:d:", ["login", "domain=", "attack="])
    except getopt.GetoptError:
        print "(optional)\n--login followed by \n -u <username> -p <password> "
        exit()

    for opt, arg in opts:
        if opt == "--login":
            isLogin = True
        elif opt == "-u":
            myUsername = arg
        elif opt == "-p":
            myPassword = arg
        elif opt == "--attack":
            attackURL = arg

    myDomainName = start()

    if isLogin:
        myHtmlGetter.setCredentials(myUsername, myPassword)
        #scrapePage(myDomainName)
        myHtmlGetter.login(myDomainName)
        myHtmlGetter.getHTML(myDomainName)

    #scrapePage(attackURL)
    #print formType
    #print myForms
    #myHtmlGetter.getForms(attackURL)
    #myHtmlGetter.mechforms(attackURL)
    myHtmlGetter.mechforms2(attackURL)
    #myHtmlGetter.getForm(attackURL)

if __name__ == "__main__":
    main(sys.argv[1:])
