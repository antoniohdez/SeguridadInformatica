import socket
# the public network interface
host = socket.gethostbyname(socket.gethostname())
# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
s.bind((host, 0))
# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
print s.recvfrom(65565)
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)