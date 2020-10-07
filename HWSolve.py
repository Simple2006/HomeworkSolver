import urllib.request
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re

n = 1
probNum = 45
pageNum = 137 #change based on which page answers are being grabbed from!

while n != 2: #change number depending on amount of problems!
    probNum = str(n)
    pageNum = str(pageNum)
    link = ("https://www.slader.com/textbook/9781608408405-algebra-2-a-common-core-curriculum/" + pageNum + "/exercises/" + probNum + "/")
    session = HTMLSession()
    req = session.get(link)
    req.html.render(timeout = 60) #change timeout times if wifi is shit!
    answer = req.html.xpath("/html/body/div[3]/section[2]/section[1]/section[3]/article[1]/section[1]/div[1]/div/div[2]/img[1]") #change xml path if site is changed!
    if len(answer) >= 1:
        answer_link = answer[0].attrs["src"]
        print("Answer for solution " + probNum + ": " + answer_link)
        image_url = answer_link
        save_name = "hw_image" + probNum + ".jpg"
        urllib.request.urlretrieve(image_url, save_name)
    else:
        print("Answer for solution " + probNum + " could not be found!")
    n = n+1
    print("-------------------------------------------------------------------------------------------------------")