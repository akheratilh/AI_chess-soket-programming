# Echo server program
import socket
from threading import Thread
from Graphic.board import Board
import json

class sock(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.host = '0.0.0.0'
        self.port = 50010
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self):
        try:
            self.s.connect((self.host, self.port)) 
            data = json.dumps({"a": Board.board})
            self.s.send(data.encode())
        except:
            print 'something wrong'

    def receive(self):
        temp = Board.board
        try:
            self.s.bind((self.host, self.port))
        except:
            print 'something wrong'
        print 'wating for connection'
        self.s.listen(1)
        conn , addr = self.s.accept()
        data = conn.recv(1024)
        data = json.loads(data.decode())
        d = data.get("a")
        for x in range (0 , 8):
            for y in range (0 , 8): 
                temp[7-x][y] = d[x][y]  
        Board.board = temp

    def close(self):
        self.s.close() 
        
    def run(self):
        #while True:
         #   s = sock()
          #  i = input('select (1.recevie  2.send) :')
           # if i == 1:
            #    s.receive()
            #elif i == 2:
             #   s.send()
            #else:
             #   s.close()
              #  break
            #s.close()
        pass
