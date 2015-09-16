from scapy.all import *
import sys, os, getopt
import thread
import time

THIS_SUMMARY =''
DEV0_RECV =True
DEV1_RECV =True


def monit_callback_dev0(pkt):
    #print 'dev0 monit'
    global THIS_SUMMARY
    global DEV0_RECV
    
    if pkt.summary() == THIS_SUMMARY:
        DEV0_RECV =True
        #print 'dev0_recv'
def monit_callback_dev1(pkt):
    #print 'dev1 monit'
    global THIS_SUMMARY
    global DEV1_RECV
    
    if pkt.summary() == THIS_SUMMARY:
        DEV1_RECV =True
        #print 'dev1_recv'

def my_sniff_dev1(localip,p):
    sniff(iface = 'eth1' ,prn=monit_callback_dev1,store=0)
def my_sniff_dev0(localip,p):
    sniff(iface = 'eth0' ,prn=monit_callback_dev0,store=0)
    
def my_send(p,localip):
    
    #thread.start_new_thread(my_sniff,(localip,p))
    global THIS_SUMMARY
    global DEV0_RECV
    global DEV1_RECV
    start_time = time.time()
    while True:
        #print DEV0_RECV,DEV1_RECV
        while DEV0_RECV ==True and DEV1_RECV==True:
            THIS_SUMMARY = p.summary()
            #print 'send' , p[IP].id
            DEV0_RECV = False
            DEV1_RECV = False
            if p[IP].src == localip:
                sendp(p,iface='eth1')
            else:
                sendp(p,iface='eth0')
            return 1
def main():

    localip = '172.16.83.107'
    pkt = rdpcap('xunlei2.pcap')
    thread.start_new_thread(my_sniff_dev1,(localip,pkt[0]))
    thread.start_new_thread(my_sniff_dev0,(localip,pkt[0]))
    for p in pkt:
        if not p.haslayer(IP):
            continue
        #print 'p.id= %d' %(p[IP].id)
        my_send(p,localip)
            
if __name__ == "__main__":
    main()
