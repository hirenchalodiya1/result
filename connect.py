import socket
import sys
import urllib.request


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))

# default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('gseb.org')
except socket.gaierror:
    # this means could not resolve the host
    print ("there was an error resolving the host")
    sys.exit()

# connecting to the server
try:
    s.connect((host_ip,port))
    print("the socket has successfully connected to google \
    on port == %s" % (host_ip))
    urllib.request.urlretrieve("http://gseb.org/522lacigam/sci/B12/34/B123456.html",'B123456.html')
except socket.error as err:
    print("Server can't Connect %s"%err)


try:
    s.close()
except socket.error as err:
    print('Error while closing server %s' %(err))