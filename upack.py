from struct import *
from scapy.all import *
def upack(pkt):
	if raw[2:4] == '\xff\xfc':
		#print "+++++++>AP Request UDP pkt<+++++++"
		d=unpack("!8B",raw[8:16])
		unpack_dict={}
		unpack_dict["ip"]=str(d[0])+"."+str(d[1])+"."+str(d[2])+"."+str(d[3])
		unpack_dict["ip_broadcast"]=str(d[4])+"."+str(d[5])+"."+str(d[6])+"."+str(d[7])
		unpack_dict["ap_mac"]=raw.encode("hex")[32:44]
		unpack_dict["ap_Version"]=raw[-226:-98]
		unpack_dict["ap_mimo"]=raw[-98:-66]
		d=unpack("!8bL",raw[-40:-28])
		unpack_dict["g24_valid"]=d[0]
		unpack_dict["g5_valid"]=d[1]
		unpack_dict["g24_txpower"]=d[2]
		unpack_dict["g5_txpower"]=d[3]
		unpack_dict["g24_channel_width"]=d[4]
		unpack_dict["g5_channel_width"]=d[5]
		unpack_dict["g24_channel_bind"]=d[6]
		unpack_dict["g5_channel_bind"]=d[7]
		unpack_dict["uptime"]=d[8]
		"""
		print "ip:\t",unpack_dict["ip"]
		print "ip_broadcast:\t",unpack_dict["ip_broadcast"]
		print "ap_mac:",unpack_dict["ap_mac"]
		print "ap_Version:\t",unpack_dict["ap_Version"]
		print "ap_mimo:\t",unpack_dict["ap_mimo"]
		print "g24_valid:\t",unpack_dict["g24_valid"]
		print "g5_valid:\t",unpack_dict["g5_valid"]
		print "g24_txpower:\t",unpack_dict["g24_txpower"]
		print "g5_txpower:\t",unpack_dict["g5_txpower"]
		print "g24_channel_width:\t",unpack_dict["g24_channel_width"]
		print "g5_channel_width:\t",unpack_dict["g5_channel_width"]
		print "g24_channel_bind:\t",unpack_dict["g24_channel_bind"]
		print "g5_channel_bind:\t",unpack_dict["g5_channel_bind"]
		print "uptime:\t\t\t",unpack_dict["uptime"]
		"""
		return unpack_dict
	elif raw[2:4] == '\xff\xfb':
		print "+++++++>AC Reply UDP<+++++++"
if __name__== "__main__":
	packet=rdpcap("./aprequest.pcap")
	raw=str(packet[0][Raw])
	pkt_info=upack(raw)
	print pkt_info["uptime"]


