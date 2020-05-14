# Echo server program
import socket
from threading import Thread
from Graphic.board import Board
from time import sleep
import json

class sock():
    def __init__(self): 
        self.host = '127.0.0.1'
        self.port = 50010
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #self.s.settimeout( 7.0)
    def send(self):
        try:
            self.s.connect((self.host, self.port)) 
        except Exception as e:
            print 'something wrong' , e 

        try:
            data = json.dumps({"a": Board.board})
            self.s.sendall(data.encode()) 
        except Exception as e:
            print 'something wrong json ' , e 
        print 'send' 

    def receive(self):
        temp = Board.board
        try:
            self.s.bind((self.host, self.port))
        except Exception as e:
            print 'something wrong' , e 
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
        print 'receive'

    def close(self):
        self.s.close() 
         
