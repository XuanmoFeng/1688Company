#!/usr/bin/env python
# coding=utf-8
import urllib
import re
import requests
import sys
import csv
import time
import codecs
reload(sys)
sys.setdefaultencoding("utf-8")
#请求地址url
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}
def getListProxies(url):
    url='http://www.xicidaili.com/nn'
    session=requests.session()
    page=session.get(url,headers=headers)
    str='class="odd".*?<td>(.*?)</td>.*?<td>(.*?)</td>(.*?)</tr>'
    res=re.findall(str,page.text,re.S)
    x=len(res)
    for i in range(0,x):
        if "HTTPS" in res[i][2]:
            proxy='https://'+res[i][0]+':'+res[i][1]
            ListCon(url,proxy)
def ListCon(url,proxy):#,cookie):
    #url2=r'https://'+url
    html=url+'/page/offerlist.htm'
    headers={
        #':authority':url,
    	#':method':'GET',
        #':path':'/page/offerlist.htm',
	#':scheme':'https',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'accept-encoding':'gzip, deflate, sdch, br',
	'accept-language':'zh-CN,zh;q=0.8',
        #'cookies':cookie,
    'referer':html,
	'upgrade-insecure-requests':'1',
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
    }
    #main=urllib.urlopen(html,headers=headers)
    #print main.read()
    MainText=requests.get(html,proxies=proxy,headers=headers,timeout=5)#,allow_redirects=False)#cookies=cookie)
    print MainText.text#.headers['Location']
    time.sleep(4)
    #li=r'<li(.*?)</li>'
    #ListNum=re.findall(li,MainText.text,re.S)
    #x=len(ListNum)
    #for i in range(0,x):
    #    print ListNum[i]
    
url='https://s.1688.com/company/company_search.htm'
Key=raw_input("请输入要搜的公司:")
Key=Key.encode('gb2312')
ipayload={'keywords':Key,'n':'y','mastheadtype':'','from':'industrySearch','industryFlag':'go'}
payload={'keywords':Key,'button_click':'top','earseDirect':'false','n':'y'}
res=requests.get(url,params=ipayload)
li=r'<li id=\"off.*?wrap\"(.*?)</li>'
compan=re.findall(li,res.text,re.S)
x=len(compan)
o=0
for i in range(0,x):
    Place=r'<a class="sm-offerResult-areaaddress".*title="(.*?)"'
    companPlace=re.findall(Place,compan[i],re.I)#公司地址
    print companPlace[0]
    companyName=r'<a class="list-item-title-text".*?>.*>(.*?)</font>(.*?)</a>'
    companyNam=re.findall(companyName,compan[i],re.S)#公司名称
    print companyNam[0][0],companyNam[0][1]
    url=r'"https://(.*?)\.1688\.com'
    companyPep=re.findall(url,compan[i],re.S)
    companyUrl='https://'+companyPep[0]+'.1688.com'
    time.sleep(5)
    print companyUrl
    #ListCon(companyUrl)#,res.cookies)
    getListProxies(companyUrl)
    #time.sleep(4)
