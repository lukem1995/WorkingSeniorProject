# Reference https://www.tutorialspoint.com/python/python_command_line_arguments.htm

import sys
import getopt
from fetcher import Fetcher

def main(argv):
    # myBrowser = Browser()
    isLogin = False
    myFetcher = Fetcher()
    username = ""
    password = ""

    try:
        opts, args = getopt.getopt(argv, "u:p:d:", ["login", "domain="])
    except getopt.GetoptError:
        print "(mandatory)\n-d <domain> or --domain <domain>" \
            " \n(optional)\n--login followed by \n -u <username> -p <password> "
        exit()

    for opt, arg in opts:
        if opt == "--login":
            isLogin = True
        elif opt == "-u":
            username = arg
        elif opt == "-p":
            password = arg
    if isLogin:
        myFetcher.setCredentials(username, password)


if __name__ == "__main__":
    main(sys.argv[1:])