from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context() # Ignore SSL certificate errors
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#actual data is http://py4e-data.dr-chuck.net/comments_685221.html
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sum=0
tags = soup('span') # Retrieve all of the span tags

for tag in tags:
   sum=sum+int(tag.contents[0])
print(sum)
