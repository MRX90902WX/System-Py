import socket
from os import system



print("\033[1;32m ____  _     _")
print("\033[1;32m/ ___|(_)___| |_ ___ _ __ ___   __ _")
print("\033[1;32m\___ \| / __| __/ _ \ '_ ` _ \ / _` |")
print("\033[1;32m ___) | \__ \ ||  __/ | | | | | (_| |")
print("\033[1;32m|____/|_|___/\__\___|_| |_| |_|\__,_|")
print("")
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

