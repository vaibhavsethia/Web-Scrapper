from bs4 import BeautifulSoup
import random
import requests

Search=input("ENTER SEARCH TERM : ")
params={"q":Search}
r=requests.get("https://www.bing.com/search",params=params)

#f=open("Dummy.html","w+")
#f.write(r.content)

soup=BeautifulSoup(r.text,"html.parser")
#print(soup.prettify())
results = soup.find("ol",{"id":"b_results"})
links = results.findAll("li",{"class":"b_algo"})

for item in links :
    Item_text=item.find("a").text
    Item_href=item.find("a").attrs["href"]

    if Item_href and Item_text :
        print (Item_text)
        print (Item_href)
        print ("Sumamry : ",item.find("a").parent.parent.find("p").text)