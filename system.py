import socket
from os import system


system("setterm -foreground green")
print("Usuario")
system("whoami")
print("\n")
print("Estado")
system("hostname")
print("\n")
print("Ip maquina")
system("hostname -i")
print("\n")
print("Ip publica")
system("curl ifconfig.me")
print("\n")
print("")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("Ip privada")
print(s.getsockname()[0])
print("\n")
print("Version ssh")
system("ssh -V")

print("")
system("bash main.sh")
