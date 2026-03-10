import socket

port =1235
address ="127.0.0.1"
BUF_SIZE = 1024

#create a socket object named client

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((address,port)) #connect to the server

message= "hello!"
client.send(bytes(message,"utf-8")) #send message to the server

data = client.recv(BUF_SIZE) #receive data from the server
client.close() #close the connection
print(data.decode("utf-8")) #decode the bytes to a string and print it