# port scanning using python
import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = input('Enter the system IP address you want to scan: ')
n = int(input('Enter the maximum number of ports to be scanned: '))
t1 = socket.gethostbyname(target)
def py_scan(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False
start = time.time()
# scanning port 0 to n-1
for port in range(n):
    if py_scan(port):
        print(f'port {port} is open')
    else:
        print(f'port {port} is closed')
end = time.time()
print(f'Time taken {end-start:.2f} seconds')
