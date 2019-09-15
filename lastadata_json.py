import json
import csv
import time
import datetime
import os
import schedule



def job():
    file = open('D:\class\B\lastdata.json','r',encoding='utf-8')


    uid = 0
    #i=0
    for line in file.readlines():
        b = json.loads(line)
        print(b)
        #i+=1
        author = b['Author']
        print(author)
        # if(author=='VIC56_CC'):
        #     print(i,author)
        uidfile = open('id.csv', 'r', encoding='utf-8')
        csvreader = csv.reader(uidfile)
        for Id_line in csvreader:
            if(Id_line[1].split()[0] == author):
                print("yes")
                #print(i)
                uid = Id_line[0].split(' ')[0]
                #print(uid)
                break
        try:
            print(uid)
        except:
            continue
        #print(line)
        out = open('D:\class\B\LastdataClassify\\test\{}.json'.format(uid), 'a', encoding='utf-8')
        print(line,file=out)
        out.close
    file.close()
    Time=datetime.datetime.now().strftime('%Y-%m-%d')
    os.rename("D:\class\B\lastdata.json","D:\class\B\\"+Time+"_lastdata.json")

if __name__ == '__main__':
    schedule.every().day.at("21:00:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

