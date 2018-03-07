# reading a website

import os,urllib
os.system ('clear')

# create a url object
uo=urllib.urlopen("http://sreeprabha.net")
fo=open("localfile.html","wb")

# read from the website and store into the local file
while True:
    s=uo.read(8192)
    if s:
        fo.write(s)
    else:
        break

fo.close()
uo.close()

# printing the headers of the website
for k, v in uo.headers.items():
    print k, "=", v
    
