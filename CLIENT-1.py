import socket
print('**************Client**************')
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sip=input("Enter the Server's IP : ")
s.connect((sip, 60000))

name=input('Enter your Name : ')
msg=name
print(' wait for few Minutes')
client=s.recv(1024)
client=client.decode("utf-8")
key=s.recv(1024)
key=key.decode("utf-8")
key=int(key)
key=key-key-key
print(key)
s.send(bytes(msg,"utf-8"))
print("***** "+client+" is on chat *****")
exmsg=bytes(client+" disconnected the connection","utf-8")
#exitm=exmsg.decode("utf-8")
#exitmsg=client+exitm
#print(exitmsg)
#print(exitm)
#msg starts
msg='HI'
l=len(msg)
m=''
for i in range(0,l):
    m=m+chr(ord(msg[i])+key)
s.send(bytes(m,"utf-8"))
while True:
    print('.....wait for '+client+'"s msg!')
    msg=s.recv(1024)
    msg=msg.decode("utf-8")
    l=len(msg)
    m=''
    for i in range(0,l):
        m=m+chr(ord(msg[i])+key)
    print(client+" : "+m)
    if m==exmsg:
        s.close()
    msg=input('You : ')
    if msg=='':
        msg='.'
    if msg=='pls_exit':
        msg=name+" disconnected the connection"
        l=len(msg)
        m=''
        for i in range(0,l):
            m=m+chr(ord(msg[i])+key)
        s.send(bytes(m,"utf-8"))
        s.close()
    else :
        l=len(msg)
        m=''
        for i in range(0,l):
            m=m+chr(ord(msg[i])+key)
        s.send(bytes(m,"utf-8"))
        
    
    
