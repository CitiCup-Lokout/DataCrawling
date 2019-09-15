import requests
import json
from time import sleep
def getHTML(html,av,pagenum):
    # count=1
    fi=open('老番茄av{}.txt'.format(av),'w',encoding='utf-8')

    for count in range(1,pagenum+1):
        url=html+str(count)
        url=requests.get(url)
        if url.status_code==200:
            cont=json.loads(url.text)
        else:
            break
        lengthRpy = len(cont['data']['replies'])
        if count==1:
            try:
                lengthHot=len(cont['data']['hots'])
                for i in range(lengthHot):
                    # 热门评论内容
                    hotMsg=cont['data']['hots'][i]['content']['message']
                    fi.write(hotMsg + '\n')
                    leng=len(list(cont['data']['hots'][i]['replies']))
                    # print(cont['data']['hots'][i]['replies'])
                    for j in range(leng):
                        # 热门评论回复内容
                        hotMsgRp=cont['data']['hots'][i]['replies'][j]['content']['message']
                        fi.write(hotMsgRp+'\n')
            except:
                pass
        if lengthRpy!=0:
            for i in range(lengthRpy):
                comMsg=cont['data']['replies'][i]['content']['message']
                fi.write(comMsg + '\n')
                # print('评论:',cont['data']['replies'][i]['content']['message'])
                try:
                    leng=len(list(cont['data']['replies'][i]['replies']))
                except:
                    leng=0
                for j in range(leng):
                    # print(cont['data']['replies'][i]['replies'])
                    comMsgRp=cont['data']['replies'][i]['replies'][j]['content']['message']
                    fi.write(comMsgRp + '\n')
        else:
            break
        print("第%d页写入成功！"%count)
        sleep(0.5)
        # count += 1
    fi.close()
    print(count,'页评论写入成功！')

url="https://api.bilibili.com/x/v2/reply?type=1&oid="

# avList=["67080029","66825348","66608963","66509570","66104657"]#敬汉卿
# countarr=[132,208,268,148,431]
# av="66825348"
# html=url+av+'&pn='
# getHTML(html,av)
# for i in range(4,5):
#     av=avList[i]
#     count=countarr[i]
#     html=url+av+'&pn='
#     getHTML(html,av,count)   


avList2=["66742079","65844602","65595759","64611629","64287119"]#老番茄
countarr2=[164,699,147,248,167]
for i in range(4,5):
    av=avList2[i]
    count=countarr2[i]
    html=url+av+'&pn='
    getHTML(html,av,count)   