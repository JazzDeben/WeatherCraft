## Free code, help yourself
## This is a python script that uses the python telnetlib to send API calls over to a Spigot Minecraft server compiled on a raspberry pi
## Note, the default username and password are being used
## the HOST here is localhost, however, this should be changed to reflect your environment
## TODO: Describe how the telnet plugin was installed on minecraft
## TODO: Document how to change username and password
## TODO: Document how to install spigot minecraft server
## TODO: include a way to fix the IP address of the minecraft server - or - pull the ip address automatically
## TODO: expand code, this is late night test start


import telnetlib

HOST = "127.0.0.1"
port = "25564"
user = b"username"
password = b"password"

tn = telnetlib.Telnet(HOST, port)

tn.write(user + b"\n")
tn.write(password + b"\n")
tn.write(b"\n")
tn.write(b"weather rain\n")
tn.close()
