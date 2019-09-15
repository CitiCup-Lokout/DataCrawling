import urllib.request
import random
import time
import json
import openpyxl
import pandas as pd
import datetime
import schedule
from itertools import islice
from urllib.request import urlopen
import collections

from multiprocessing import Process
import os


outdate = []
lastdata = []
useless = []
ForMat = ['AVNum','Topic','Type','UploadTime','Author','DMNum','Comment','Save','Coin','Like','Duration','Original','View']

def requests_headers(): #构造请求头池
    head_connection = ['Keep-Alive','close']
    head_accept = ['text/html,application/xhtml+xml,*/*']
    head_accept_language = ['zh-CN,fr-FR;q=0.5','en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
    head_user_agent = [
      "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
      "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
      "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
      "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
      "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
      "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
      "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
      "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
      "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
      "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
      "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
      "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
      "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
      "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
      "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
      "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
      "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
      "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
      "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
      "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
      "UCWEB7.0.2.37/28/999",
      "NOKIA5700/ UCWEB7.0.2.37/28/999",
      "Openwave/ UCWEB7.0.2.37/28/999",
      "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
      # iPhone 6：
    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",]

    header = {
        'Connection':head_connection[random.randrange(0,len(head_connection))],
        'Accept':head_accept[0],
        'Accept-Language':head_accept_language[random.randrange(0,len(head_accept_language))],
        'User-Agent':head_user_agent[random.randrange(0,len(head_user_agent))],
    } #获得随机请求头
    return header

proxies = ['112.85.168.43:9999']

def request_proxie():
    header1 = requests_headers ()  # 获得随机请求头
    proxie_handler = urllib.request.ProxyHandler({'http':random.choice(proxies)})
    opener = urllib.request.build_opener(proxie_handler)
    header = []
    for key,value in header1.items():
        elem = (key,value)
        header.append(elem)
    opener.addheaders = header
    a = [opener,header1]
    return a


def getHtmlInfo(av_num):
    try:
      print("start")
      time.sleep(0.5)
      m = request_proxie()
      opener = m[0]
      req_view = opener.open("https://api.bilibili.com/x/web-interface/view?aid=" + str(av_num),timeout=12)
      page_view = req_view.read().decode('utf-8')
      
      dic_page = json.loads(page_view)  # 将获取内容转成字典形式
    #print(m[1])
    
    except:

      
      videodata=[[],[],[],[],[],[],[]]
      return videodata
    #print(dic_page)
    
    if dic_page['code'] != 0:  # 判断视频是否存在，不存在返回av号及错误原因
        video_data = [av_num, dic_page['message'], dic_page['code'], '', '', '', '', '', '', '']
        print(video_data[1])
        #useless.append(int(av_num))
    else:

        """
        依次获取视频av号、视频标题、视频类型、上传时间、作者（UP主）、弹幕数、评论数、收藏数、投币数、点赞数、是否转载
        """
        #print(av_num)
        video_info = dic_page['data']
        #print(video_info['copyright'])
        print("getinfo")
        if(video_info['copyright'] == 1):

            video_data = [video_info['aid'],  # av号
                          video_info['title'],  # 标题
                          video_info['tname'],  # 视频类型
                          time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(video_info['ctime'])),
                          # 上传时间，网页获取时间为Unix时间戳，转换成一般时间显示模式
                          video_info['owner']['name'],  # 作者
                         # video_info['stat']['view'],
                          video_info['stat']['danmaku'],  # 弹幕数
                          video_info['stat']['reply'],  # 评论数
                          video_info['stat']['favorite'],  # 收藏数
                          video_info['stat']['coin'],  # 投币数
                          video_info['stat']['like'],  # 点赞数
                          video_info['duration'],
                          "原创",
                          video_info['stat']['view']
                          ]
            startTime = datetime.datetime.strptime(video_data[3],'%Y-%m-%d %H:%M:%S')
            a = (datetime.datetime.now()-startTime).days
            if(a>=7):
              outdate.append(int(video_data[0]))
            #print(outdate)

            #exit()
        else:
            video_data = [video_info['aid'],  # av号
                          video_info['title'],  # 标题
                          video_info['tname'],  # 视频类型
                          time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(video_info['ctime'])),
                          # 上传时间，网页获取时间为Unix时间戳，转换成一般时间显示模式
                          video_info['owner']['name'],  # 作者
                          #video_info['stat']['view'],
                          video_info['stat']['danmaku'],  # 弹幕数
                          video_info['stat']['reply'],  # 评论数
                          video_info['stat']['favorite'],  # 收藏数
                          video_info['stat']['coin'],  # 投币数
                          video_info['stat']['like'],  # 点赞数
                          video_info['duration'],
                          "非原创",
                          video_info['stat']['view']
                          ]
            startTime = datetime.datetime.strptime(video_data[3],'%Y-%m-%d %H:%M:%S')
            a = (datetime.datetime.now()-startTime).days
            if(a>=7):
              outdate.append(int(video_data[0]))

       # time.sleep(1 + random.randint(-1, 2))


    req_view.close()

    return video_data
def main():
    outdate.clear()
    useless.clear()
    lastdata.clear()
    Time = datetime.datetime.now().strftime('%m-%d %H')
    source = open('newvideo.txt','r',encoding='utf-8')
    #print("test")
    AVNum=[]
    Topic=[]
    Type=[]
    UploadTime=[]
    Author=[]
    View = []
    DMNum=[]
    Comment=[]
    Save=[]
    Coin=[]
    Like=[]
    Duration=[]
    Original=[]
    aids = source.readlines()
    total = len(aids)
    iter = 0
    start = time.time()
    for aidp in aids:
        aid = aidp.split('\n')[0]
        videodata = getHtmlInfo(aid)
        print(str(iter+1)+'/'+str(total))
        iter+=1
        #print(videodata[3])
        if(len(videodata)<12):
          print("incomplete info")
          continue
        for i in range(len(videodata)):
          if(videodata[i]==""):
            print("fail to get info")
            continue
        try:
            print(videodata)
            if(int(aid) in outdate):
              lastdata.append(videodata)
            else:
            #print("test")
             # print(videodata)
              AVNum.append(videodata[0])
              Topic.append(videodata[1])
              Type.append(videodata[2])
              UploadTime.append(videodata[3])
              Author.append(videodata[4])
             # View.append(videodata[5])
              DMNum.append(videodata[5])
              Comment.append(videodata[6])
              Save.append(videodata[7])
              Coin.append(videodata[8])
              Like.append(videodata[9])
              Duration.append(videodata[10])
              Original.append(videodata[11])
              View.append(videodata[12])
            print("success")
        except:
            print("fail to get info")
            a = len(Original)
            if(len(AVNum)>a):
                AVNum.pop()
            if(len(Topic)>a):
                Topic.pop()
            if(len(Type)>a):
                Type.pop()
            print(aid)
            pass
        #iter+=1
            # print(video_data,file=videoinfo)
    out = open('newvideo.txt','w',encoding='utf-8')
    oldvideo = open('lastdata.json','a',encoding='utf-8')



    jsondict = []

    for i in range(len(lastdata)):
        print(ForMat)
        print(lastdata[i])
        d = collections.OrderedDict()
        for j in range(len(ForMat)):
          d[ForMat[j]]=lastdata[i][j]

        jsondata=json.dumps(d)

        print(jsondata,file=oldvideo)


    print(outdate)
    for aidp in aids:
      #if(int(aidp) in useless):
       # print(aidp)
        #continue
      if(int(aidp) in outdate):
        print(aidp)
        continue
      else:
        print(int(aidp),file=out)


    res=pd.DataFrame({'AVNum':AVNum,'Topic':Topic,'Type':Type,'UploadTime':UploadTime,\
            'Author':Author,'DMNum':DMNum,'Comment':Comment,'Save':Save,'Coin':Coin,'Like':Like,'Duration':Duration,'Original':Original,'View':View})
    res.to_csv("{}.csv".format(Time),index=False)
    print("time:", time.time() - start)

if __name__ == "__main__":
    #print("test")
    #main()
    #schedule.every().day.at("01:15:10").do(main)
    #schedule.every().day.at("04:15:01").do(main)
    #schedule.every().day.at("07:15:10").do(main)
    #schedule.every().day.at("10:15:01").do(main)
    #schedule.every().day.at("13:15:10").do(main)
    #schedule.every().day.at("16:15:01").do(main)
    #schedule.every().day.at("19:45:10").do(main)
    #schedule.every().day.at("22:15:01").do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
