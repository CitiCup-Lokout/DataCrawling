# -*- coding:utf-8 -*-
import datetime
import pandas as pd
from itertools import islice
from urllib.request import urlopen
import requests
import urllib.request
import random
import time
from time import sleep
import json
uplist=open('uplist.csv','r',encoding='utf-8')
uidl=[]
Namel=[]
Levell=[]
Genderl=[]
Profilel=[]
Timel=[]
FanNuml=[]
PlayNuml=[]
ChargeNuml=[]
iter=0
for line in islice(uplist, 1, None):
    Time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    Timel.append(Time)
    i=line.split(',')[0].strip(' ')
    uidl.append(i)
    # i=3
    # print(i)
    Basicurl="https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp".format(i)
    Fanurl="https://api.bilibili.com/x/relation/stat?vmid={}&jsonp=jsonp".format(i)
    Playurl="https://api.bilibili.com/x/space/upstat?mid={}&jsonp=jsonp".format(i)
    Chargeurl="https://elec.bilibili.com/api/query.rank.do?mid={}&type=jsonp&jsonp=jsonp".format(i)
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36' }
    r = requests.get(Basicurl,headers=headers)
    r.encoding = 'utf-8'
    # a=r.text
    # print(json.loads(a)['data']['sex'])

    basicsjson = r.text
    dic_page = json.loads(basicsjson)
    Name=dic_page['data']['name']
    Namel.append(Name)
    Level=dic_page['data']['level']
    Levell.append(Level)
    Gender=dic_page['data']['sex']
    Genderl.append(Gender)
    Profile=dic_page['data']['sign']
    Profilel.append(Profile)

    r = requests.get(Fanurl,headers=headers)
    r.encoding = 'utf-8'
    Fanjson = r.text
    dic_page = json.loads(Fanjson)
    FanNum=dic_page['data']['follower']
    FanNuml.append(FanNum)
    try:
        response = requests.get(Playurl,headers=headers)
        response.encoding = 'utf-8'
        Playjson = response.text
        dic_page = json.loads(Playjson)
        PlayNum=dic_page['data']['archive']['view']
        PlayNuml.append(PlayNum)
    except:
        PlayNuml.append(None)
    try:
        response = requests.get(Chargeurl,headers=headers)
        r.encoding = 'utf-8'
        r = response.text
        Chargejson = json.loads(r.replace('(','')[4:-1])
        ChargeNum=Chargejson['data']['count']
        # print(ChargeNum)
        ChargeNuml.append(ChargeNum)
    except:
        ChargeNuml.append(None)
    iter+=1
    sleep(0.3)
    if iter==100 or iter==500 or iter==1000 or iter==1500 or iter==2000 or iter==2500:
        print("iter: ",iter)
    #if iter==5:
     #  break
res=pd.DataFrame({'uid':uidl,'Name':Namel,'Level':Levell,'Gender':Genderl,'Profile':Profilel,'Time':Timel,\
    'FanNum':FanNuml,'PlayNum':PlayNuml,'ChargeNum':ChargeNuml})
res.apply(pd.to_numeric, errors='ignore')

print("111")
res.to_json("upProfile.json",force_ascii=False,orient='records')

