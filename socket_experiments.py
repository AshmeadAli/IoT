import socket               # Import socket module

print("creating socket..")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("done.")

print ("connecting to remote host..")
s.connect(("www.python.org",80))
print("done.")

print("connected from", s.getsockname())
print( "connected to", s.getpeername())
       

