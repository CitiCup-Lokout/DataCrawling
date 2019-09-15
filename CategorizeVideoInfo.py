###################

# 新建一个和B文件夹同级的文件夹，如upvideo, 将此文件和压缩文件中的up主文件们放入 #

#########################################################
# AVNum,Topic,Type,UploadTime,Author,Duration,DMNum,Comment,Save,Coin,Like,Original
import pandas as pd
import schedule
import os
import csv
import time

def addinfo():
    # check_new_file=open('/media/freyameng/DATA1/1myfolder/Ratatouille/citiBank/DataClear/upVideo/aPreviousFileName','r',encoding='utf-8')
    check_new_file=open('/root/upVideo/aPreviousFileName','r',encoding='utf-8')
    oldFiles=[]
    for line in check_new_file:
        oldFiles.append(line.strip("\n"))#将所有已归类的文件名存到oldFiles列表
    check_new_file.close()
    filepath = '/root/B'
    # filepath='/media/freyameng/DATA1/1myfolder/Ratatouille/citiBank/DataClear/B'
    arr=os.listdir(filepath)

    # check_new_file=open('/media/freyameng/DATA1/1myfolder/Ratatouille/citiBank/DataClear/upVideo/aPreviousFileName','a+',encoding='utf-8')
    check_new_file=open('/root/upVideo/aPreviousFileName','a+',encoding='utf-8')
    
    
    iter=0
    for Curfile in arr:#arr 里是current file(更新后的目录) oldFile是之前的目录
        iter+=1
        if Curfile not in oldFiles:#如果当前的文件名不在oldFile列表中，将当前文件归类
            print('归类新文件ing:',Curfile)
            print(Curfile,file=check_new_file)
            addfilename=Curfile
            #print(Curfile)
            try:
                # print(addfilename)
                # addfile=pd.read_csv('/media/freyameng/DATA1/1myfolder/Ratatouille/citiBank/DataClear/B/{}'.format(addfilename),encoding='utf-8')
                addfile=pd.read_csv('/root/B/{}'.format(addfilename),encoding='utf-8')

                tmp=addfile.AVNum[0]
                for i in range(len(addfile.AVNum)):
                    Author=addfile.Author[i]
                    file_name = Author
                    t_flag = 0
                    # ID = open('/media/freyameng/DATA1/1myfolder/Ratatouille/citiBank/DataClear/id.csv', 'r', encoding='utf-8')
                    ID = open('/root/id.csv', 'r', encoding='utf-8')
                    csvreader = csv.reader(ID)
                    for line in csvreader:
                        if(t_flag==0):
                            t_flag+=1
                            #print("test")
                            continue
                        else:
                            #print(line[1].split()[0])
                            if(line[1].split()[0] == file_name):
                                uid = line[0].split(' ')[0]
                                # print(uid,line[1].split()[0],file_name)
                    ID.close()
                    time.sleep(0.1)
                    # basisfile=open("/media/freyameng/DATA1/1myfolder/Ratatouille/citiBank/DataClear/upVideo/{}.json".format(uid),'a+',encoding='utf-8')
                    basisfile=open("/root/upVideo/{}.json".format(uid),'a+',encoding='utf-8')
                    try:
                        resdf=pd.DataFrame({'CrawlTime':[addfilename],'AVNum':[addfile.AVNum[i]],'Topic':[addfile.Topic[i]],'Type':[addfile.Type[i]],\
                        'UploadTime':[addfile.UploadTime[i]],'Author':[addfile.Author[i]],'Duration':[addfile.Duration[i]],\
                        'DMNum':[addfile.DMNum[i]],'Comment':[addfile.Comment[i]],'Save':[addfile.Save[i]],\
                        'Coin':[addfile.Coin[i]],'Like':[addfile.Like[i]],'Original':[addfile.Original[i]],'View':[addfile.View[i]]})
                    except:#如果没有View
                        try:
                            resdf=pd.DataFrame({'CrawlTime':[addfilename],'AVNum':[addfile.AVNum[i]],'Topic':[addfile.Topic[i]],'Type':[addfile.Type[i]],\
                            'UploadTime':[addfile.UploadTime[i]],'Author':[addfile.Author[i]],'Duration':[addfile.Duration[i]],\
                            'DMNum':[addfile.DMNum[i]],'Comment':[addfile.Comment[i]],'Save':[addfile.Save[i]],\
                            'Coin':[addfile.Coin[i]],'Like':[addfile.Like[i]],'Original':[addfile.Original[i]]})
                        except:#如果没有duration
                            resdf=pd.DataFrame({'CrawlTime':[addfilename],'AVNum':[addfile.AVNum[i]],'Topic':[addfile.Topic[i]],'Type':[addfile.Type[i]],\
                            'UploadTime':[addfile.UploadTime[i]],'Author':[addfile.Author[i]],\
                            'DMNum':[addfile.DMNum[i]],'Comment':[addfile.Comment[i]],'Save':[addfile.Save[i]],\
                            'Coin':[addfile.Coin[i]],'Like':[addfile.Like[i]],'Original':[addfile.Original[i]]})
                    print(resdf.to_json(force_ascii=False,orient='records'),file=basisfile)
                    # print(resdf.to_json(force_ascii=False,orient='records'))
            except:
                print(addfilename,'中无AVNum')


        # if iter==6:
        #     break
        
        
        
def main():
    # addinfo()
    #schedule.every().day.do(addinfo)#每天加一次？
	schedule.every().day.at("00:00:01").do(addinfo)
	schedule.every().day.at("12:00:00").do(addinfo)
	while True:
		#print("111")
		schedule.run_pending()
		time.sleep(1)
if __name__ == "__main__":
    main()

# filePath = 'D:\\1myfolder\\Ratatouille\\citiBank\\DataClear\\B'
# arr=os.listdir(filePath)
# res=pd.DataFrame({'PreviousFileNum':arr})
# res.to_csv('PreviousFileName.csv',index=False,encoding='utf-8')

