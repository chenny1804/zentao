# -*- coding: cp936 -*-
import base64
import urllib2
import httplib
import urllib

def authentication(username,password):
    return 'Basic '+base64.encodestring('%s:%s'%(username,password))[:-1]

def set_cgi(cgi,cgi_parm,lan_addr,user=None,passwd=None,):
    global check_pppoe_set_ok
    httpheader={
                'Accept-Encoding':'deflate',
                'Connection':'keep-alive',
                'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36',
                'content-type':'application/x-www-form-urlencoded'}
    if type(cgi_parm) !=dict:
        raise 'cgi_info should be a dict'
    
    if user !=None and passwd!=None:
        Authorization=authentication(user,passwd)
        httpheader['Authorization']=Authorization

    reurl=cgi
    params=urllib.urlencode(cgi_parm)
    #print params
    try:
        conn=httplib.HTTPConnection(lan_addr)
    except Exception as e:
        print '连接lan_addr失败' ,e
        
    #print 'connnect router success'

        
    try:
        conn.request(method="POST",url=reurl,body=params,headers=httpheader)
    except Exception as e:
        print "请求cgi失败",e

    try:
        response=conn.getresponse()
        res = response.read()
    except Exception as e:
        print "返回失败",e  
    if res=='''["SUCCESS"]''':
        print "set cgi SUCCESS"
        return True
    else:
        check_pppoe_set_ok=False
        return False

def init_cgi_parm(cgi_file):
    f = open(cgi_file,'r')
    cgi_value={}
    for i in f.readlines():
        #print i
        cgi_value[i.split('\t')[0].strip()]=i.split('\t')[-1].strip()
    #print cgi_value
    return cgi_value

'''def main():
    tmp_cgi=init_cgi_parm('D:\chariot_auto\NW730\cgi_static.txt')
    cgi = '/cgi-bin-igd/netcore_set.cgi'
    set_cgi(cgi,tmp_cgi,'192.168.1.1','','')
    
#main()
'''
