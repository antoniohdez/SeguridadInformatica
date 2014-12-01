#!/usr/bin/env python
import socket
import subprocess
import sys

def scan(option = 1):
    remoteServer    = raw_input("Enter a remote host to scan: ")
    remoteServerIP  = socket.gethostbyname(remoteServer)

    print "-" * 60
    print "Please wait, scanning remote host: ", remoteServerIP
    print "-" * 60

    try:
        for port in range(1,1025):  
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((remoteServerIP, port))
            if result == 0:
                output = "Port " + str(port) + ": \t Open\n"
                if option == 1:
                    print output
                elif option == 2:
                    save_output(output)

            s.close()

    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()

    except socket.error:
        print "Couldn't connect to server"
        sys.exit()

    print 'Scanning Completed'

def save_output(output):
    with open("nmap.txt", "a") as f:    
        f.write(output)