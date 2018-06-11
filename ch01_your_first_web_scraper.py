from bs4 import BeautifulSoup
from urllib.error import (
    HTTPError,
    URLError,
)
from urllib.request import urlopen


try:
    html = urlopen('http://pythonscraping.com/pages/page1')
except (HTTPError, URLError, ValueError) as e:
    print(e)
    raise SystemExit

bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.h1)
print(bs.html.body.h1)
print(bs.body.h1)
print(bs.html.h1)
