import json
import math



with open("IP.txt") as f:
    content = f.read().splitlines()

    ipAddresses = []
    for i in content:
        ipAddresses.append((i.split(" ")[0], i.split(" ")[1]))
        print(ipAddresses)
