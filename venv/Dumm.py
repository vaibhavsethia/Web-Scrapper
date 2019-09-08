from bs4 import BeautifulSoup
import random
import requests

Search=input("ENTER SEARCH TERM : ")
params={"q":Search}
r=requests.get("https://www.bing.com/search",params=params)

soup=BeautifulSoup(r.text,"html.parser")
Results = soup.find("ol",{"id":"b_results"})