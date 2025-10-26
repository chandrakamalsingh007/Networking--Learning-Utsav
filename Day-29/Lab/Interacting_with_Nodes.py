from netmiko import ConnectHandler
import csv

ip_list = []

with open('Day-29/Lab/hosts.csv') as csvfile:

    readCSV = csv.reader(csvfile, delimiter=';')
    for row in readCSV:
        # Avoid empty column at the end due to trailing semicolon
        if row[1].strip():
            ip_list.append(row[1])

print("Collected IPs: ", ip_list)

for ip in ip_list:
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "admin",
        "password": "admin",
        "secret": "admin",  # If enable password is needed
    }

    try:
        connection = ConnectHandler(**device)
        connection.enable()
        output = connection.send_command("show ip interface brief")
        print(f"\n✅ Output from {ip}")
        print(output)
        connection.disconnect()
    except Exception as e:
        print(f"\n❌ Could not connect to {ip} → {e}")


