#Built in Method in python

IP = "172.16.10.1"
#print(dir(IP))

#New_IP= IP.replace("172","192").replace("16","168")
New_IP = IP.split(".")
print(New_IP)

