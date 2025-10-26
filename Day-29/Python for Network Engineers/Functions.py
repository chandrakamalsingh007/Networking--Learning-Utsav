#Functions in python

def ospf_process (process_id, network, mask, area):
    print(f" router ospf {process_id} \n network {network} {mask} area {area}")


ospf_process("10", "10.1.1.0", "255.255.255.0", "50")