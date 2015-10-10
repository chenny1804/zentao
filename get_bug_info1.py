import httplib
import urlparse
 
def request(url, cookie=''):
    ret = urlparse.urlparse(url)    # Parse input URL
    if ret.scheme == 'http':
        conn = httplib.HTTPConnection(ret.netloc)
    elif ret.scheme == 'https':
        conn = httplib.HTTPSConnection(ret.netloc)
        
    url = ret.path
    if ret.query: url += '?' + ret.query
    if ret.fragment: url += '#' + ret.fragment
    if not url: url = '/'
    
    conn.request(method='GET', url=url , headers={'Cookie': cookie})
    return conn.getresponse()
if __name__ == '__main__':
    cookie_str="sid=dui44gm2u2o3uf0d0r1mdjqae4;lastProduct=34;qaBugOrder=id_desc;theme=default;"
    url = 'http://192.168.2.165/zentao/project-bug-46.html'
    html_doc = request(url, cookie_str).read()
    print html_doc
