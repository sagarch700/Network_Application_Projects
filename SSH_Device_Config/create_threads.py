import threading

def create_threads(ip_list, function):

    threads = []

    for ip in ip_list:
        th = threading.Thread(target= function, args= (ip,))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()
