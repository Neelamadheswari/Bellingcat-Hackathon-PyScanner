# port scanning using python
import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = input('Enter the system IP address you want to scan: ')
n = int(input('Enter the maximum number of ports to be scanned: '))
t1 = socket.gethostbyname(target)
def py_scan(port):
    try:
        s.connect((t1, port))
        return True
    except:
        return False
start = time.time()
for i in range(n):
    if py_scan(i):
        print(f'port {i} is open')
    else:
        print(f'port {i} is closed')
end = time.time()
print(f'Time taken {end-start:.2f} seconds')
