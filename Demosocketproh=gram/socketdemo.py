import  socket
# print(socket.gethostbyname(socket.gethostname()))
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("www.google.com",80))