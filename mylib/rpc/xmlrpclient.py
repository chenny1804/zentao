import xmlrpclib

server = xmlrpclib.ServerProxy("http://127.0.0.1:8080")
print server.ix.test("adfa1230",1,"Throughput.scr",6,"192.168.1.100","192.168.1.102",10)
print server.ix.test("adfa1230",0,"Throughput.scr",6,"192.168.1.100","192.168.1.102",10)
#������ testid,target,script,pairNum,e1,e2,duration
#�������壺
#testid   �����׵�ID��һ��������Ψһһ��
#target   ����call��Ŀ�ģ�
#           0 ����ID����testid�Ĳ����ף�
#           1 �½�һ��IDΪtestId�Ĳ����ף������������pair������ΪpairNum
#           2 ��ID����testId�Ĳ����������pair������ΪpairNum
#e1       pair��Դ��IP��ַ����targetΪ0ʱ������
#e2       pair���޶�IP��ַ����targetΪ0ʱ������
#duration ���Գ���ʱ�䣨�룩����targetΪ0ʱ������
#
#
#���ӣ�
#step1�� server.ix.test("abc1234",1,"Throughput.scr",3,"192.168.1.101","192.168.1.103",30)
#   ���һ�����Ϊabc1234�Ĳ��ԣ�pair����Ϊ3����"192.168.1.101"��"192.168.1.103"
#   ����30�룬����ֵΪ��xmlrpc_c::value_double��0.0
#step2�� server.ix.test("abc1234",2,"Response_Time.scr",3,"192.168.1.102","192.168.1.101",25)
#   ��test abc1234�����3��pair����"192.168.1.102"��"192.168.1.101"��
#   ��������test�Ľű���ΪResponse_Time.scr������ʱ���Ϊ25������ֵΪ��xmlrpc_c::value_double��0.0
#step3�� server.ix.test("abc1234",0,"Response_Time.scr",3,"192.168.1.102","192.168.1.101",25)
#   �����޸�test abc1234���κ����ݣ�ֻ������
#   ����ֵΪ��xmlrpc_c::value_double�����Խ��������

#������ͬ�� testid����Ѿ���ִ�й���������step3ֻ�᷵���ϴεĽ��

