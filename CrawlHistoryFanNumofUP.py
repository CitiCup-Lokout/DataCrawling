import time
import csv
import re
import pickle
import json
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from multiprocessing import Process
import os
from itertools import islice
import pandas as pd
uidList=[]
NameList=[]
# List812=[]
# uplist=open('result.csv','r+',encoding="utf-8")
df=pd.read_csv('histFan201812.csv')
# print(df.uid[0])
iter=0
for i in range(len(df)):
    uid=df.uid[i]
    uidList.append(uid)
    Name=df.Name[i]
    NameList.append(Name)
length=len(NameList)
# List812=[None]*length
# List91=[None]*length
# List92=[None]*length
# List93=[None]*length
# List94=[None]*length
List95=[None]*length
List96=[None]*length
# print(List812[:10])
driver = webdriver.Chrome()
# # 2018-12
# url='http://leptc.github.io/bili/2018/all.html'
# driver.get(url)
# NumPerPage=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"example_length\"]/label/select/option[4]")))
# NumPerPage.click()
# for i in range(50):
#     nextpage = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"example_next\"]")))
#     for i in range(1,101):
#         NamePath="//*[@id=\"example\"]/tbody/tr["+str(i)+"]/td[2]"
#         Name=driver.find_element_by_xpath(NamePath).text
#         if Name in NameList:
#             idx=NameList.index(Name)
#             FanNum=driver.find_element_by_xpath("//*[@id=\"example\"]/tbody/tr["+str(i)+"]/td[3]").text
#             List812[idx]=FanNum
#     nextpage.click()

# #2019-01
# url='http://leptc.github.io/bili/2019/01/all.html'
# driver.get(url)
# NumPerPage=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"example_length\"]/label/select/option[4]")))
# NumPerPage.click()
# for i in range(60):
#     nextpage = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"example_next\"]")))
#     for i in range(1,101):
#         NamePath="//*[@id=\"example\"]/tbody/tr["+str(i)+"]/td[1]"
#         Name=driver.find_element_by_xpath(NamePath).text
#         if Name in NameList:
#             # print(Name)
#             idx=NameList.index(Name)
#             FanNum=driver.find_element_by_xpath("//*[@id=\"example\"]/tbody/tr["+str(i)+"]/td[2]").text
#             List91[idx]=FanNum
#     nextpage.click()

# #2019-02
# url='http://leptc.github.io/bili/2019/02/'
# driver.get(url)
# NumPerPage=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"example_length\"]/label/select/option[4]")))
# NumPerPage.click()
# for i in range(60):
#     nextpage = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"example_next\"]")))
#     for i in range(1,101):
#         NamePath="//*[@id=\"example\"]/tbody/tr["+str(i)+"]/td[1]/a"
#         Name=driver.find_element_by_xpath(NamePath).text
#         if Name in NameList:
#             # print(Name)
#             idx=NameList.index(Name)
#             FanNum=driver.find_element_by_xpath("//*[@id=\"example\"]/tbody/tr["+str(i)+"]/td[2]").text
#             List92[idx]=FanNum
#     nextpage.click()

# #2019-03
# url='http://leptc.github.io/bili/2019/03/'
# driver.get(url)
# NumPerPage=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"example_length\"]/label/select/option[4]")))
# NumPerPage.click()
# for i in range(60):
#     nextpage = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"example_next\"]")))
#     for i in range(1,101):
#         NamePath="//*[@id=\"example\"]/tbody/tr["+str(i)+"]/td[1]/a"
#         Name=driver.find_element_by_xpath(NamePath).text
#         if Name in NameList:
#             # print(Name)
#             idx=NameList.index(Name)
#             FanNum=driver.find_element_by_xpath("//*[@id=\"example\"]/tbody/tr["+str(i)+"]/td[2]").text
#             List93[idx]=FanNum
#     nextpage.click()

# #2019-04
# url='http://leptc.github.io/bili/2019/04/'
# driver.get(url)
# NumPerPage=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"example_length\"]/label/select/option[4]")))
# NumPerPage.click()
# for i in range(60):
#     nextpage = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"example_next\"]")))
#     for i in range(1,101):
#         NamePath="//*[@id=\"example\"]/tbody/tr["+str(i)+"]/td[1]/a"
#         Name=driver.find_element_by_xpath(NamePath).text
#         if Name in NameList:
#             # print(Name)
#             idx=NameList.index(Name)
#             FanNum=driver.find_element_by_xpath("//*[@id=\"example\"]/tbody/tr["+str(i)+"]/td[2]").text
#             List94[idx]=FanNum
#     nextpage.click()
# tmpdf=pd.DataFrame({'uid':uidList,'Name':NameList,'2018-12':List812\
#         ,'2019-01':List91,'2019-02':List92,'2019-03':List93,'2019-04':List94\
#             })
# tmpdf.to_csv('HistFanNum1904.csv',index=False)

#2019-05
url='http://leptc.github.io/bili/2019/05/'
driver.get(url)
for i in range(1,6001):
    NamePath="//*[@id=\"example\"]/tbody/tr["+str(i)+"]/td[1]/a"
    Name=driver.find_element_by_xpath(NamePath).text
#     print(Name)
    if i%100==0:
        print('i',i)
    if Name in NameList:
        idx=NameList.index(Name)
        FanNum=driver.find_element_by_xpath("//*[@id=\"example\"]/tbody/tr["+str(i)+"]/td[2]").text
        # print(FanNum)
        
        List95[idx]=FanNum
        print(idx,FanNum)
    # if i==10:
    #     break
fivedf=pd.DataFrame({'uid':uidList,'Name':NameList,\
                # '2018-12':List812,'2019-01':List91,'2019-02':List92,'2019-03':List93,'2019-04':List94,\
                    '2019-05':List95
                    })
fivedf.to_csv('HistFanNumOonly95.csv',index=False)

# #2019-06
# url='http://leptc.github.io/bili/2019/06/a.html'
# driver.get(url)
# for i in range(1,4001):
#     NamePath="//*[@id=\"example\"]/tbody/tr["+str(i)+"]/td[1]/a"
#     Name=driver.find_element_by_xpath(NamePath).text
#     if Name in NameList:
#         idx=NameList.index(Name)
#         FanNum=driver.find_element_by_xpath("//*[@id=\"example\"]/tbody/tr["+str(i)+"]/td[2]").text
#         List96[idx]=FanNum


# resdf=pd.DataFrame({'uid':uidList,'Name':NameList,\
#     # '2018-12':List812,'2019-01':List91,'2019-02':List92,'2019-03':List93,'2019-04':List94,\
#         '2019-05':List95,'2019-06':List96\
#         })
# resdf.to_csv('HistFanNum.csv',index=False)
