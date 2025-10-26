IP = "172.16.10.1"


New_IP = IP.split(".")
print(type(New_IP))

# print(New_IP[0])
# print(New_IP[2])
# print(New_IP[0:2])

# New_IP.append("255.255.255.0")
# print(New_IP)

New_IP.sort()
print(New_IP)