# coding:utf-8
import datetime

from itertools import islice
from urllib.request import urlopen

from multiprocessing import Process

import urllib.request
import random
import time
import json
import os
import schedule


# print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))   #日期格式化
newvideo = []            # 新视频的AV号

def requests_headers():  # 构造请求头池
    head_connection = ['Keep-Alive', 'close']
    head_accept = ['text/html,application/xhtml+xml,*/*']
    head_accept_language = ['zh-CN,fr-FR;q=0.5', 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
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
        'Connection': head_connection[random.randrange(0, len(head_connection))],
        'Accept': head_accept[0],
        'Accept-Language': head_accept_language[random.randrange(0, len(head_accept_language))],
        'User-Agent': head_user_agent[random.randrange(0, len(head_user_agent))],
    }  # 获得随机请求头
    return header


proxies = ['163.204.245.47:9999']


def request_proxie():
    header1 = requests_headers()  # 获得随机请求头
    proxie_handler = urllib.request.ProxyHandler({'http': random.choice(proxies)})
    opener = urllib.request.build_opener(proxie_handler)
    header = []
    for key, value in header1.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


def check():
    Time = datetime.datetime.now().strftime('%m-%d %H')
    uplist = open('a.csv', 'r', encoding='utf-8')
    number_init = open('init.txt', 'r', encoding='utf-8')

    numberlist=[]
    a = number_init.readlines()
    for number in a:
        num = number.split('\n')
        numberlist.append(num[0])

    number_init.close()
    res = open('newvideo.txt', 'a', encoding="utf-8") # newvideo file

    opener = request_proxie()

    iter = 0
    for line in islice(uplist, 1, None):
        print(str(iter)+"/"+str(len(numberlist)))
        time.sleep(0.3)


        i = line.split(', ')[0].strip(' ')

        #print(i, end=",", file=res)
        videourl = "https://space.bilibili.com/ajax/member/getSubmitVideos?mid={}&page=1&pagesize=100".format(i)

        try:

            r = opener.open(videourl,timeout=12)
        except:
            print("timeout")
            continue
        try:
            Videojson = r.read().decode('utf-8')
        except:
            print("incomplement read")
            continue

        dic_page = json.loads(Videojson)
        try:
            print(numberlist[iter])

            videonum = dic_page['data']['count']
            author = dic_page['data']['vlist'][0]['author']
            print(videonum)
            print(author)
            print(videonum == int(numberlist[iter]))
            if(videonum > int(numberlist[iter])):               #检查是否发布新视频
                videoinfo = dic_page['data']['vlist']
                if(videoinfo):
                    print(videonum-int(numberlist[iter]))
                    print(videoinfo)
                    if(videonum-int(numberlist[iter])>15):
                        numberlist[iter]= videonum
                    for i in range(videonum-int(numberlist[iter])):
                        newvideo.append(videoinfo[i]['aid'])    #存储新视频的AV号
                    numberlist[iter] = videonum                 #更新列表
            else:
            	numberlist[iter] = videonum
        except:
            print("noinfo")
            break

        iter += 1
    #print(newvideo)
    number_now = open('init.txt', 'w', encoding='utf-8')
    for num in numberlist:
        print(num,file=number_now)
    for i in range(len(newvideo)):
        #print(newvideo[i])
        print(newvideo[i],file=res)

    number_now.close()
    res.close()


# def firstsearch(a):
#     opener = request_proxie()
#     uplist = open('a.csv', 'r', encoding='utf-8')
#     videonumber = open('3.txt', 'w', encoding='utf-8')
#     # iter = 0
#     for line in islice(uplist, 1, None):
#         time.sleep(0.5)


#         i = line.split(', ')[0].strip(' ')
#         videourl = "https://space.bilibili.com/ajax/member/getSubmitVideos?mid={}&page=1&pagesize=100".format(i)


#         r = opener.open(videourl)
#         Videojson = r.read().decode('utf-8')

#         dic_page = json.loads(Videojson)

#         try:
#             videonum = dic_page['data']['count'] #
#             print(i,videonum,file=videonumber)

#         except:

#             print(i,'noinfo',file=videonumber)
#             print("noinfo")

#     return a

def maintrace():
    start = time.time()
   # initlist = []                       #最初始的upvideo数
   # firstsearch(initlist)

    p = Process(target=check)           #每3小时check一次
    p.start()
    p.join()
    print("time:", time.time() - start)


def main():
    start = time.time()
   # initlist = []                       #最初始的upvideo数
   # firstsearch(initlist)
    # print("test")
   # maintrace()
    schedule.every().day.at("01:00:01").do(maintrace)
    #schedule.every().day.at("03:00:01").do(maintrace)
    #schedule.every().day.at("06:00:00").do(maintrace)
    #schedule.every().day.at("09:00:01").do(maintrace)
    #schedule.every().day.at("12:00:00").do(maintrace)
    #schedule.every().day.at("15:00:01").do(maintrace)
    #schedule.every().day.at("18:02:00").do(maintrace)
    #schedule.every().day.at("21:00:01").do(maintrace)

    #p = Process(target=check)           #每3小时check一次
    #p.start()
    #p.join()
    #print("time:", time.time() - start)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()




