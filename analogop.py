# -*- coding: cp936 -*-
import urllib
import urllib2
import cookielib
import sys
import re
from time import sleep
from bs4 import BeautifulSoup
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)
# default header
postd = {'account': 'luoss',
         'password': '123456',
         'referer':'/zentao/'
         } 
HEADER = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
    'Referer' : 'http://192.168.2.165'
}
# operate method
def geturlopen(hosturl, postdata = {}, headers = HEADER):
    # encode postdata
    enpostdata = urllib.urlencode(postdata)
    # request url
    try:
        urlrequest = urllib2.Request(hosturl, enpostdata, headers)
    # open url
        urlresponse = urllib2.urlopen(urlrequest)
    except Exception,e:
        print  "无法建立网络连接，请检查你的url是否正确"
        sys.exit(1)
    # return url
    return urlresponse
def checkmsg(response):
    if response.msg == 'OK':
        return response
    else:
        return False
def login(url):
    response = geturlopen(url, postd)
    return checkmsg(response)
def findItem(item):
    url="http://192.168.2.165/zentao/project-ajaxGetMatchedItems-"+item+"-project-task-unclosed.html"
    response = geturlopen(url)
    return checkmsg(response)
def getItem_Bug(task_num):
    url="http://192.168.2.165/zentao/project-bug-"+task_num+".html"
    response = geturlopen(url)
    return checkmsg(response)
def main(item_list):
    for i in item_list:
        Item_bug=getItem_Bug(i.split("-")[2])
        html_doc=Item_bug.read().decode("utf-8")
        soup = BeautifulSoup(html_doc,"html5lib")
        bug_num=soup.findAll("tr",'text-center')
        bug_value=soup.findAll("input")
        #print len(bug_num)
        BUG_ID=str(bug_value[2]).split("value=")[1].split("\"")[1]
        #print BUG_ID
    return len(bug_num),BUG_ID
if __name__ == "__main__":
    ITEM="NAC100"
    user_login = login('http://192.168.2.165/zentao/user-login.html')
    if user_login:
        if user_login.read().decode('utf-8').find("/zentao/index.html") > 0:
            print "login Success!!!"
        else:
            print "Lon is Error"

    else:
        print "Login is Error"
        exit(0)
    Item=findItem(ITEM)
    item_list=[]
    for i in Item.readlines():
        if i.decode("utf-8").find('href') > 0:
            item_list.append(i.split("' ")[0].split("\'")[1])
    first_bug_num,first_bug_id=main(item_list)
    print "latest_bug_num:",first_bug_num,"latest_bug_id:",first_bug_id
    while True:
        latest_bug_num,latest_bug_id=main(item_list)
        if latest_bug_num-first_bug_num:
            first_bug_num=latest_bug_num
            first_bug_id=latest_bug_id
        else:
            print "no bug update",ITEM
        sleep(3600)

