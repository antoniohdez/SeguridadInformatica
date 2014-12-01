#!/usr/bin/env python
import socket
import sys
from struct import *
def sniffer(option = 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    except socket.error , msg:
        print msg
        sys.exit()

    while True:
        packet = s.recvfrom(65535)
        packet = packet[0]
        ip_header = packet[0:20] # first 20 characters
        iph = unpack('!BBHHHBBH4s4s' , ip_header)
        
        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
        iph_length = ihl * 4
        ttl = iph[5]
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8]);
        d_addr = socket.inet_ntoa(iph[9]);

        output = 'Version : ' + str(version) + '\n' + 'IP Header Length : ' + str(ihl) + '\n' + 'TTL : ' + str(ttl) + '\n' + 'Protocol : ' + str(protocol) + '\n' + 'Source Address : ' + str(s_addr) + '\n' + 'Destination Address : ' + str(d_addr)+ "\n"
        if option == 1:
            print output
        elif option == 2:
            save_output(output)
        
        tcp_header = packet[iph_length:iph_length+20]
        tcph = unpack('!HHLLBBHHH' , tcp_header)
        
        source_port = tcph[0]
        dest_port = tcph[1]
        sequence = tcph[2]
        acknowledgement = tcph[3]
        doff_reserved = tcph[4]
        tcph_length = doff_reserved >> 4
        
        output = 'Source Port : ' + str(source_port) + '\n' + 'Dest Port : ' + str(dest_port) + '\n' + 'Sequence Number : ' + str(sequence) + '\n' + 'Acknowledgement : ' + str(acknowledgement) + '\n' + 'TCP header length : ' + str(tcph_length) + '\n'
        if option == 1:
            print output
        elif option == 2:
            save_output(output)
        
        h_size = iph_length + tcph_length * 4
        data_size = len(packet) - h_size
        
        data = packet[h_size:] #data
        
        if option == 1:
            print repr(data)
        elif option == 2:
            save_output(repr(data))


def save_output(output):
    with open("sniffer.txt", "a") as f:    
        f.write(output)




