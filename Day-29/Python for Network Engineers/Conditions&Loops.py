devices = { 
   "R1":"IOS",
    "R2":"IOS-XR",
    "R3":"NX-05"
}

'''
node = input()

if node in devices:
    print(f"I can configure {devices[node]}")
else:
    print("I don't know about these devices")
'''

for items in devices:
    print(items)

for key,value in devices.items():
    print(key,value)