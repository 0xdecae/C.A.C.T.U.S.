import time, socket, scapy
    start = time.perf_counter()
    
    i = 1

    # while time.perf_counter() - start > duration:
    #     for source_port in range(1, 65535):
    #         IP1 = IP(source_IP = source_IP, destination = target_IP)
    #         TCP1 = TCP(srcport = source_port, dstport = 80)
    #         pkt = IP1 / TCP1
    #         send(pkt, inter = .001)
    #         i = i + 1
    return i, socket.gethostname()