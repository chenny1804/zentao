# -*- coding: cp936 -*-
from login_email import login_email
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import os.path
import mimetypes
#from email.header import Header
class Email:
    def __init__(self,To_address,name="tester"):
        self.to_address=To_address
        self.name=name
        self.content=self.name+":"+u"\n  您好！\n\t性能自动化测试已完成，结果见附件"
        self.main_msg = MIMEMultipart()
    def send(self):
        server=login_email()
        self.main_msg_fun()
        try:
            server.sendmail("netcoretester@163.com", self.to_address, self.main_msg.as_string())
            print "邮件发送成功，注意查收"
        finally:
            server.quit()
    def main_msg_fun(self):
        text_msg=MIMEText(self.content,_charset="gb2312")
        #text_msg=MIMEText(self.content,'text',_charset="utf-8")
        self.main_msg['From']="netcoretester@163.com"
        if type(self.to_address) == list:
            self.main_msg['To']=','.join(self.to_address)
        else:
            self.main_msg['To']=self.to_address
        self.main_msg['Subject'] = u"禅道bug提示"
        self.main_msg['Date'] = email.Utils.formatdate()
        self.main_msg.attach(text_msg)
    def set_content(self,content):
        self.content=self.name+":"+u"\n  您好！\n\t"+content
    def add_file(self,file_name):
        contype = 'application/octet-stream'
        maintype, subtype = contype.split('/', 1)
        data=open(file_name,"rb")
        file_msg = MIMEBase(maintype, subtype)
        file_msg.set_payload(data.read( ))
        data.close()
        email.Encoders.encode_base64(file_msg)
        basename = os.path.basename(file_name)
        file_msg.add_header('Content-Disposition',
                            'attachment', filename = basename)
        self.main_msg.attach(file_msg)
        
if __name__=="__main__":
    email_list=['773552385@qq.com','chenyue1804@126.com']
    seml=Email(email_list,name="陈悦")
    seml.set_content("有新bug了")
    #seml.add_file(".\confi.txt")
    seml.send()  
