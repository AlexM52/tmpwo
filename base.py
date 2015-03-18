import socket

def main():
    print "Starting process...\n Creating socket..."
    srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Binding socket.."
    srvsock.bind((socket.gethostname(), 8080))
    srvsock.listen(2)
    print "Listening.\n"
    
    #loop
    while True:
        (c, addr) = srvsock.accept()
        print "Connection from : ", addr
        msg = c.recv(4096)
        print msg
        c.close()
        
    #srvsock.close()
    
main()