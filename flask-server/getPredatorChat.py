import requests 
from bs4 import BeautifulSoup
import numpy as np
import os
import csv
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
for g in newPedosList:
    response=requests.get(link+g)
    if response.status_code==200:
        soup=BeautifulSoup(response.text,'html.parser')
    chatsToAppend=soup.find_all('span',class_='code_chat')
    chatText=[]
    chunk_size=500000
    for i in chatsToAppend:
        chat_text=i.get_text(strip=True)
        for f in range(0,len(chat_text),chunk_size):
            chats.append([chat_text[f:f+chunk_size],1])

path=r'C:\Users\USER\Downloads\pedoChatLogsv2.csv'

with open(path,'w',newline='',encoding='utf-8') as file:
    writer=csv.writer(file)
    writer.writerows(chats)
