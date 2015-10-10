# -*- coding: cp936 -*-
import ConfigParser
import os
import sys
class Read_ini:
    def __init__(self,path):
        self.conf=ConfigParser.ConfigParser()
        if os.path.exists(path):
            self.read(path)
        else:
            print "文件不存在"
            sys.exit()
    def read(self,path):
        self.conf.read(path)
    def get_section(self):
        return  self.conf.sections()
    def get_items(self,section):
        return self.conf.items(section)
    def get_value(self,section,key):
        return self.conf.get(section,key)

if __name__=="__main__":
    rd=Read_ini(".\chariot_test.ini")
    sc=rd.get_section()
    print sc
    items=rd.get_items(sc[0])
    print items
    model = rd.conf.get("VersionInfo","model")
    version = rd.conf.get("VersionInfo","version")
    sdk = rd.conf.get("VersionInfo","sdk")
    password = rd.get_value("wirelessinfo","password")
    print password
    if sdk == "":
        print sdk,"sdk 为空"
    else:
        print "sdk"
