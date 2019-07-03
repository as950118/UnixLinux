import os
from selenium import webdriver

query = str(input().encode("euc-kr"))
url="https://www.google.com/search?q="+query+"&newwindow=1&source=lnms&tbm=isch"

wd = webdriver.Chrome()
wd.get(url)
elems = wd.find_element_by_xpath("//img[@src]")
print(elems.text)
for elem in elems:
    print(elem.text)
