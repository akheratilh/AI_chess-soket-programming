# Echo server program
import socket
from threading import Thread

class sock():
    def __init__(self):
        self.host = '0.0.0.0'
        self.port = 50010
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    def send(self , msg):
        try:
            self.s.connect((self.host, self.port)) 
            self.s.send(msg)
        except:
            print 'something wrong'
        
    
    def receive(self):
        try:
            self.s.bind((self.host, self.port))
        except:
            print 'something wrong'
        print 'wating for connection'
        self.s.listen(1)
        conn , addr = self.s.accept()
        d = conn.recv(1024) 
        print addr , d
        

    def close(self):
        self.s.close()

class co(Thread):
    def __init__(self):
        Thread.__init__(self) 
        
    def run(self):
        while True:
            s = sock()
            i = input('select (1.recevie  2.send) :')
            if i == 1:
                s.receive()
            elif i == 2:
                msg = raw_input('enter message: ')
                s.send(msg)
            else:
                s.close()
                break
            s.close()

