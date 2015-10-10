# -*- coding: cp936 -*-
import io
import os

class ping_test():

    def ping(self,dst_ip):
        str1="请求超时"
        str2="无法访问目标主机"
        cmd=os.popen("ping "+dst_ip+" -n 2")
        lines=cmd.readlines()
        for line in lines:
            if (str1 in line) or (str2 in line):
                print line
                return 0
        return 1      
    def check_link(self,dst_ip):
        count=0
        index=0
        print "检测链路通断情况"
        while count < 10:
            if self.ping(dst_ip):
                count=count+1
                print "ping ",count," ",
            elif index <10:
                count=0
                index=index+1
                print "第",index,"次检测"
            if index >=20:
                print "\n链路不同"
                return False
        print "\n链路正常"
        return True
if __name__=="__main__":
    p=ping_test()
    print p.check_link("10.0.0.65")
