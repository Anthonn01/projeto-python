import socket

url = input("digite uma url")

ip = socket.gethostbyname(url)

print(ip)

print(socket.gethostbyname("https"))