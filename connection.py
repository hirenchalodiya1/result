import socket

host = 'gseb.org'
port = 80
path = '/'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))
print('socket connected')
request_header = 'GET /285soipmahc/ssc/B82/17/B8217807.html HTTP/1.1\r\nHost: www.gseb.org\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nReferer: http://www.gseb.org/\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-IN,en;q=0.9,en-US;q=0.8,gu;q=0.7,hi;q=0.6'
# request = f'GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: keep-alive\r\nAccept-language: en'
req = bytes(request_header, 'utf-8')
print('request sent')
req_code = sock.send(req)
print('awaitinng response')
res = sock.recv(65536)
print(res)
