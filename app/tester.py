import requests 
from bs4 import BeautifulSoup
import numpy as np
import os
url='http://www.perverted-justice.com/?con=full'
response=requests.get(url)
if response.status_code==200:
    soup=BeautifulSoup(response.text,'html.parser')
pedos=soup.find_all('a',id='pedoLink')
newPedosList=[]
for i in pedos:
    newPedosList.append(i.text)
chats=[]
link="http://www.perverted-justice.com/?archive="
for g in newPedosList[0:30]:
    response=requests.get(link+g)
    if response.status_code==200:
        soup=BeautifulSoup(response.text,'html.parser')
    chatsToAppend=soup.find_all('span',class_='code_chat')
    chatText=[]
    for i in chatsToAppend:
        chat_text=i.get_text(strip=True)
        chats.append(chat_text)
print(len(chats))
#path=r'C:\Users\USER\Downloads\pedoChatLogs.txt'

#with open(path,'w',encoding="utf-8") as file:
 #   for chat in chats:
  #      file.write(chat+"\n")
