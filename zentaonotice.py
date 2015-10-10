# -*- coding: cp936 -*-
import urllib
import urllib2
import cookielib
import sys
import re
from time import sleep
from bs4 import BeautifulSoup
from mylib.email.Email_lib import Email
from mylib.readini.read_ini import Read_ini
import time

rd=Read_ini(".\conf.ini")

ITEM=rd.get_value("config","item").split("|")
EMAIL=rd.get_value("config","email").split("|")
INTER_TIME=int(rd.get_value("config","time"))
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)
# default header
postd = {'account': 'cheny',
         'password': 'chy851',
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
        return 'NOK'
    # return url
    return urlresponse
def checkmsg(response):
    if response == 'NOK':
        return False
    elif response.msg == 'OK':
        return response
    else:
        return False
def login(url):
    response = geturlopen(url, postd)
    return checkmsg(response)
def findItem(item):
    url="http://192.168.2.165/zentao/project-ajaxGetMatchedItems-"+urllib.quote(item.decode("cp936").encode('utf-8'))+"-project-task-unclosed.html"
    print sys.stdin.encoding
    response = geturlopen(url)
    return checkmsg(response)
def getItem_Bug(task_num):
    url="http://192.168.2.165/zentao/project-bug-"+task_num+".html"
    response = geturlopen(url)
    return checkmsg(response)
def send_email(email_list,names,content):
    seml=Email(email_list,names)
    seml.set_content(content)
    seml.send()
def analysis_buglist(item_list):
    for i in item_list:
        Item_bug=getItem_Bug(i.split("-")[2])
        html_doc=Item_bug.read().decode("utf-8")
        soup = BeautifulSoup(html_doc)
        bug_num=soup.findAll("strong")
        bug_name1=soup.findAll("td")
        bug_title=soup.findAll("title")
        bug_href=soup.findAll("a")
        #print bug_href
        #for i in range(0,len(bug_href)):
        #    if str(bug_href[i]).decode("utf-8").find("/zentao/bug-view-") and str(bug_href[i]).decode("utf-8").find("target=\"_blank\"")  > 0:
        #        print i, str(bug_href[i]).decode("utf-8").split('href=\"')[1].split('\" ')[0]
        BUG_CREATOR=str(bug_name1[4]).split('>')[1].split('<')[0]
        BUG_RD=str(bug_name1[5]).split('>')[1].split('<')[0]
        BUG_TITLE=str(bug_name1[3]).split("=\"")[2].split('\"')[0]
        bug_value=soup.findAll("input")
        BUG_ID=str(bug_value[2]).split("value=")[1].split("\"")[1]
        BUG_NUM=str(bug_num[0]).split('>')[1].split('<')[0]
        #print BUG_NUM
    return int(BUG_NUM),BUG_ID,BUG_CREATOR,BUG_RD,BUG_TITLE
def main():
    user_login = login('http://192.168.2.165/zentao/user-login.html')
    if user_login:
        if user_login.read().decode('utf-8').find("/zentao/index.html") > 0:
            print "login Success!!!"
        else:
            print "ERROR"
    dic_ITEM={}
    for  item in ITEM:
        Item=findItem(item)
        #print Item
        dic_ITEM[item]={}
        dic_ITEM[item]["item_web_list"]=[]
        for line in Item.readlines():
            #print line
            if line.decode("utf-8").find('href') > 0:
                #print line.split("' ")[0].split("\'")[1]
                dic_ITEM[item]["item_web_list"].append(line.split("\' ")[0].split("\'")[1])
                dic_ITEM[item]["first_bug_num"],dic_ITEM[item]["first_bug_id"],dic_ITEM[item]["first_bug_creator"],dic_ITEM[item]["first_bug_rd"],dic_ITEM[item]["first_bug_title"]=analysis_buglist(dic_ITEM[item]["item_web_list"])
        #print dic_ITEM[item]["item_web_list"]
                #print item," latest_bug_num:",dic_ITEM[item]["first_bug_num"],"latest_bug_id:",dic_ITEM[item]["first_bug_id"]
    while True:
        for item in ITEM:
            latest_bug_num,latest_bug_id,latest_bug_creator,latest_bug_rd,latest_bug_title=analysis_buglist(dic_ITEM[item]["item_web_list"])
            bug_num=latest_bug_num-dic_ITEM[item]["first_bug_num"]
            if bug_num:
                dic_ITEM[item]["first_bug_num"]=latest_bug_num
                dic_ITEM[item]["first_bug_id"]=latest_bug_id
                dic_ITEM[item]["first_bug_creator"]=latest_bug_creator
                dic_ITEM[item]["first_bug_rd"]=latest_bug_rd
                dic_ITEM[item]["first_bug_title"]=latest_bug_title
                content0=u"项目:[ "+item.decode('cp936')+u" ]在禅道有"+str(bug_num)+u"个新bug!详情见禅道\n"+u"最新bug编号为:"+dic_ITEM[item]["first_bug_id"]+"\t"
                content1=u"由 "+latest_bug_creator.decode('utf-8')+u" 提交给 "+latest_bug_rd.decode('utf-8')+"\n"
                content3=u"BUG描述："+latest_bug_title.decode('utf-8')+"\n"
                content=content0+content1+content3
                send_email(EMAIL,"To ALL",content)
            else:
                print time.strftime('%Y-%m-%d %H:%M:%S'),item,"no bug update"
        sleep(INTER_TIME)
'''
def getBugCreattime():
    user_login = login('http://192.168.2.165/zentao/user-login.html')
    if user_login:
        if user_login.read().decode('utf-8').find("/zentao/index.html") > 0:
            print "login Success!!!"
        else:
            print "Lon is Error"
    else:
        print "Login is Error"
        sys.exit(0)
    dic_ITEM={}
    ITEM=["NAC100"]
    for  item in ITEM:
        Item=findItem(item)
        #print Item
        dic_ITEM[item]={}
        dic_ITEM[item]["item_web_list"]=[]
        for line in Item.readlines():
            #print line
            if line.decode("utf-8").find('href') > 0:
                #print line.split("' ")[0].split("\'")[1]
                dic_ITEM[item]["item_web_list"].append(line.split("\' ")[0].split("\'")[1])
                dic_ITEM[item]["first_bug_num"],dic_ITEM[item]["first_bug_id"],dic_ITEM[item]["first_bug_creator"],dic_ITEM[item]["first_bug_rd"],dic_ITEM[item]["first_bug_title"]=analysis_buglist(dic_ITEM[item]["item_web_list"])
        #print dic_ITEM[item]["item_web_list"]
                print item," latest_bug_num:",dic_ITEM[item]["first_bug_num"],"latest_bug_id:",dic_ITEM[item]["first_bug_id"]
'''    
if __name__ == "__main__":
    main()
    #getBugCreattime()

