import socket
import smtplib
import socket

#socket.AF_INET,socket.SOCK_STREAM
print('**************Server**************')
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((socket.gethostbyname(socket.gethostname()),60000))
s.listen(5)
print('listening',(socket.gethostbyname(socket.gethostname()),60000))
print('Tell client to enter the above IP address..')
clientsocket,address=s.accept()
name=input('Enter your Name : ')
msg=name
clientsocket.send(bytes(msg,"utf-8"))
key=int(input('Enter integer value between 0 to 10 : '))
key=str(key)
clientsocket.send(bytes(key,"utf-8"))
key=int(key)
client=clientsocket.recv(1024)
client=client.decode("utf-8")
print("***** "+client+" is on chat *****")
exmsg=bytes(client+" disconnected the connection","utf-8")
#msg starts
while True:
    msg=clientsocket.recv(1024)
    msg=msg.decode("utf-8")
    l=len(msg)
    m=''
    for i in range(0,l):
        m=m+chr(ord(msg[i])+key)
    print(client+" : "+m)
    if msg==exmsg:
        clientsocket.close()
    msg=input('You : ')
    if msg=='':
        msg='.'
    if msg=='pls_exit':
        print('You disconnected the connection !!!')
        msg=name+" disconnected the connection"
        l=len(msg)
        m=''
        for i in range(0,l):
            m=m+chr(ord(msg[i])+key)
        clientsocket.send(bytes(m,"utf-8"))
        clientsocket.close()
    else :
        l=len(msg)
        m=''
        for i in range(0,l):
            m=m+chr(ord(msg[i])+key)
        clientsocket.send(bytes(m,"utf-8"))
    print('.....wait for '+client+'"s msg!')
   
  
