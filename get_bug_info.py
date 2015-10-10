import urllib
import urllib2
import cookielib
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)
HEADER = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0',
    'Referer' : 'http://192.168.2.165/zentao/user-login-L3plbnRhby8=.html',
    'Host':"192.168.2.165",
    'Connection':'keep-alive'
}
  
POSTDATA = {
    'account': 'fanky',
    'password': '123456',
    'referer':'/zentao/'
}
   
HOSTURL = 'http://192.168.2.165/zentao/user-login-L3plbnRhby8=.html'
  
enpostdata = urllib.urlencode(POSTDATA)
urlrequest = urllib2.Request(HOSTURL,enpostdata,HEADER)
urlresponse = urllib2.urlopen(urlrequest)
print urlresponse.read()
'''
#print cj
cookie_str="sid=dui44gm2u2o3uf0d0r1mdjqae4;lastProduct=34;qaBugOrder=id_desc;theme=default;"
url ="http://192.168.2.165/zentao/bug-view-8338.html"
req= urllib2.Request(url)
res_data = urllib2.urlopen(req)
print res_data.read()
html_doc = request(url, cookie_str).read()
print html_doc
'''
