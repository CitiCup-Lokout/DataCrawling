#coding:utf-8
import datetime

from itertools import islice
from urllib.request import urlopen

from multiprocessing import Process
import schedule
import urllib.request
import random
import time
import json
import os
import pandas as pd

# print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))   #日期格式化
def requests_headers(): #构造请求头池
    head_connection = ['Keep-Alive','close']
    head_accept = ['text/html,application/xhtml+xml,*/*']
    head_accept_language = ['zh-CN,fr-FR;q=0.5','en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
    head_user_agent = ['Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                       'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                       'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                       'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                       'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']
    header = {
        'Connection':head_connection[random.randrange(0,len(head_connection))],
        'Accept':head_accept[0],
        'Accept-Language':head_accept_language[random.randrange(0,len(head_accept_language))],
        'User-Agent':head_user_agent[random.randrange(0,len(head_user_agent))],
    } #获得随机请求头
    return header

proxies = ['125.66.217.114:6675','112.251.161.82:6675',
'117.34.253.157:6675','113.94.72.209:6666',
'114.105.217.144:6673','125.92.110.80:6675',
'112.235.126.55:6675','14.148.99.188:6675',
'112.240.161.20:6668','122.82.160.148:6675',
'175.30.224.66:6675']

def request_proxie():
    header1 = requests_headers ()  # 获得随机请求头
    proxie_handler = urllib.request.ProxyHandler({'http':random.choice(proxies)})
    opener = urllib.request.build_opener(proxie_handler)
    header = []
    for key,value in header1.items():
        elem = (key,value)
        header.append(elem)
    opener.addheaders = header
    return opener

def bcrawl():
    
    '''
    proxies = ["125.66.217.114:6675"
        ,"112.251.161.82:6675"
# '117.34.253.157:6675','113.94.72.209:6666',
# '114.105.217.144:6673','125.92.110.80:6675',
# '112.235.126.55:6675','14.148.99.188:6675',
# '112.240.161.20:6668','122.82.160.148:6675',
# '175.30.224.66:6675'\
    ]'''
    Time = datetime.datetime.now().strftime('%m-%d %H')
    print(Time,"start Crawling....")
    uplist=open('uplist.csv','r',encoding='utf-8')
    res=open('{}.csv'.format(Time), 'w',encoding="utf-8")
    # uplist=open('D:\\1myfolder\\Ratatouille\\citiBank\\BiliCrawler\\a.csv','w')
    # res=open('D:\\1myfolder\\Ratatouille\\citiBank\\BiliCrawler\\res.csv', 'w',encoding="utf-8")
    print("uid,Time,FanNum,PlayNum,ChargeNum",file=res)
    opener = request_proxie()
    iter=0
    for line in islice(uplist, 1, None):
        #print(uplist.read())
        Time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        Nocharge=0
        NoPlayNum=0
        i=line.split(', ')[0].strip(' ')
        print(iter)
        Fanurl="https://api.bilibili.com/x/relation/stat?vmid={}&jsonp=jsonp".format(i)
        Playurl="https://api.bilibili.com/x/space/upstat?mid={}&jsonp=jsonp".format(i)
        Chargeurl="https://elec.bilibili.com/api/query.rank.do?mid={}&type=jsonp&jsonp=jsonp".format(i)
        headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36' }
        
        # proxy_support = request.ProxyHandler(proxies)
        # #创建Opener
        # opener = request.build_opener(proxy_support)
        # #添加User Angent
        # opener.addheaders = [('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')]
        # #安装OPener
        # request.install_opener(opener)
        # #使用自己安装好的Opener
        # response = request.urlopen(Fanurl)

        r = opener.open(Fanurl)
        Fanjson = r.read().decode('utf-8')
        dic_page = json.loads(Fanjson)

        FanNum=dic_page['data']['follower']
        # print("fan",FanNum)
        try:
            # response = requests.get(Playurl,headers=headers)
            #print("test")
            response = opener.open(Playurl)
            Playjson = response.read().decode('utf-8')
            dic_page = json.loads(Playjson)
            PlayNum=dic_page['data']['archive']['view']
            # print("play",PlayNum)

        except:
            NoPlayNum=1

        try:
            response = opener.open(Chargeurl)
            # response = requests.get(Chargeurl,proxies=proxies)
            r = response.read().decode('utf-8')
            Chargejson = json.loads(r.replace('(','')[4:-1])
            ChargeNum=Chargejson['data']['count']
            # print(ChargeNum)
        except:
            Nocharge=1

        if Nocharge==0 and NoPlayNum==0:
            print(i,",",Time,",",FanNum,",",PlayNum,",",ChargeNum,file=res)
        elif Nocharge==1:
            print(i,",",Time,",",FanNum,",",PlayNum,",",file=res)
        else:
            print("no play and charge: ",i)
            print(i,",",Time,",",FanNum,",",file=res)
        iter+=1
        # if iter==100 or iter==500 or iter==1000 or iter==1500 or iter==2000 or iter==2500:
        #     print("iter: ",iter)
        if iter%100==0:
            print("iter: ",iter)
        #if iter==1:
          #  break
    res.close()

def job():
    # start=time.time()
    p = Process(target=bcrawl)
    p.start()
    p.join()

def main():
    # schedule.every(1).hour.do(job)
    # schedule.every(1).minutes.do(job)
    schedule.every().day.at("00:00:01").do(job)
    # schedule.every().day.at("01:00:00").do(job)
    # schedule.every().day.at("02:00:00").do(job)
    schedule.every().day.at("03:00:00").do(job)
    # schedule.every().day.at("04:00:00").do(job)
    # schedule.every().day.at("05:00:00").do(job)
    schedule.every().day.at("06:00:00").do(job)
    # schedule.every().day.at("07:00:00").do(job)
    # schedule.every().day.at("08:00:00").do(job)
    schedule.every().day.at("09:00:00").do(job)
    # schedule.every().day.at("10:00:00").do(job)
    # schedule.every().day.at("11:00:00").do(job)
    schedule.every().day.at("12:00:00").do(job)
    # schedule.every().day.at("13:00:00").do(job)
    # schedule.every().day.at("14:00:00").do(job)
    schedule.every().day.at("15:00:00").do(job)
    # schedule.every().day.at("16:00:00").do(job)
    # schedule.every().day.at("17:00:00").do(job)
    schedule.every().day.at("18:00:00").do(job)
    # schedule.every().day.at("19:00:00").do(job)
    # schedule.every().day.at("20:00:00").do(job)
    schedule.every().day.at("21:00:00").do(job)
    # schedule.every().day.at("22:00:00").do(job)
    # schedule.every().day.at("23:00:00").do(job)


    # schedule.every().day.at("13:34:00").do(job)


    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()

    


