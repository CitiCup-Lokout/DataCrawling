import codecs
import matplotlib.pyplot as plt
import numpy as np
from snownlp import SnowNLP
from snownlp import sentiment
from snownlp.sentiment import Sentiment
from matplotlib.pyplot import *
import os
import pandas as pd

def snowanalysis(self,filename):
    fields=filename.split("av")
    print(fields)
    sentimentslist = []
    num=0
    for li in self:
        s = SnowNLP(li)
        if(s.sentiments>0.5):
            num+=1
        sentimentslist.append(s.sentiments)
    print(sentimentslist[:5])
    # resdf=pd.DataFrame({'up':[fields[0]],'av':[fields[1]],'SentimentScore':[sentimentslist]})
    # basisfile=open("VideoSentiment.csv",'a+',encoding='utf-8')
    # basisfile=open("VideoSentiment.json",'a+',encoding='utf-8')
    print(float(num/len(sentimentslist)))
    plt.hist(sentimentslist,bins=np.arange(0,1,0.01))
    plt.figure(figsize=(10.24,9.99))
    plt.ylabel('Number of Comments')
    plt.xlabel('Sentiment score:  Negative--Positive')
    plt.savefig('./changedimg/'+filename.rstrip('.txt')+'.png')
    plt.show()
    # print(resdf.to_csv(index=False),file=basisfile)

    # print(resdf.to_json(force_ascii=False,orient='records'),file=basisfile)

filepath='./Comments'
arr=os.listdir(filepath)

# for i in range(len(arr)):
for i in range(1,10):
    comment=[]
    path = './Comments/'+arr[i]
    with open(path,'r') as f:
        rows=f.readlines()
        for row in rows:
            if (row != '\n'):
                if row not in comment:
                    comment.append(row.strip('\n'))
    print(i,'\n',comment[:5])

    snowanalysis(comment,arr[i].strip('.txt'))
    
