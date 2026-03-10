import socket
port =1235
address ="127.0.0.1"
buf_size = 1024

#create a socket object named server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((address,port))  #telling its a server port 
server.listen(5) #queue up to 5 clients
print("Server is listening on port")

while True:
    con,addr =server.accept()
    print("Connection from",addr)
    data=con.recv(buf_size) #receive data from the client
    print(data.decode("utf-8")) #decode the bytes to a string and print it
    con.send(data) #echo the data back to the client