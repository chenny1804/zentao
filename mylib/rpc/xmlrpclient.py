import xmlrpclib

server = xmlrpclib.ServerProxy("http://127.0.0.1:8080")
print server.ix.test("adfa1230",1,"Throughput.scr",6,"192.168.1.100","192.168.1.102",10)
print server.ix.test("adfa1230",0,"Throughput.scr",6,"192.168.1.100","192.168.1.102",10)
#参数表： testid,target,script,pairNum,e1,e2,duration
#参数释义：
#testid   测试套的ID，一个测试有唯一一个
#target   本次call的目的：
#           0 运行ID等于testid的测试套，
#           1 新建一个ID为testId的测试套，并向其中添加pair，数量为pairNum
#           2 向ID等于testId的测试套中添加pair，数量为pairNum
#e1       pair的源端IP地址，当target为0时被忽略
#e2       pair的宿端IP地址，当target为0时被忽略
#duration 测试持续时间（秒），当target为0时被忽略
#
#
#例子：
#step1： server.ix.test("abc1234",1,"Throughput.scr",3,"192.168.1.101","192.168.1.103",30)
#   添加一个编号为abc1234的测试，pair数量为3，从"192.168.1.101"到"192.168.1.103"
#   运行30秒，返回值为（xmlrpc_c::value_double）0.0
#step2： server.ix.test("abc1234",2,"Response_Time.scr",3,"192.168.1.102","192.168.1.101",25)
#   向test abc1234中添加3个pair，从"192.168.1.102"到"192.168.1.101"，
#   并将整个test的脚本改为Response_Time.scr，运行时间改为25，返回值为（xmlrpc_c::value_double）0.0
#step3： server.ix.test("abc1234",0,"Response_Time.scr",3,"192.168.1.102","192.168.1.101",25)
#   不会修改test abc1234的任何内容，只运行它
#   返回值为（xmlrpc_c::value_double）测试结果吞吐量

#假如相同的 testid编号已经被执行过，再运行step3只会返回上次的结果

