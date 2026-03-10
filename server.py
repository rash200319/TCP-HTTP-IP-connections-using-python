import socket
port =1234
address ="127.0.0.1"

#create a socket object named server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((address,port))  #telling its a server port 
server.listen(5) #queue up to 5 clients
print("Server is listening on port")

while True:
    con,addr =server.accept()
    print("Connection from",addr)
    con.send(bytes("Welcome to the server","utf-8")) #can use any unicode character set, utf-8 is common