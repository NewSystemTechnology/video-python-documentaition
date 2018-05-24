import socket

def get_remote_host_ip(Host):
    try:
        ip = socket.gethostbyname(Host)
        print("IP Address from {} Host IS: {}".format(Host,ip))
    except socket.error as err:
        print("{} {}".format(Host,err))
    

        
if __name__ == '__main__':
    get_remote_host_ip("python.org")
    
