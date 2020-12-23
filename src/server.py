import socket
from _thread import *
import sys

server="192.168.43.193"
port=5555

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#if port is unavailable
try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server started, waiting for connection")

#parallel process to stack up connections and avoid delay
#start_new_thread() won't have to wait for this to finish
def threaded_client(conn):
    conn.send(str.encode("Connected"))
    while True:
        try:
            data=conn.recv(2048)
            reply=data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received ",reply) 
                print("Sending ",reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()

#listen for incoming connections continuously, store connection(object) and address(IP)
while True:
    conn,addr=s.accept()
    print("Connected to ",addr)
    
    start_new_thread(threaded_client,(conn,))
