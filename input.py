import json
import math
import ipinfo
import sys # used for maximum integer constant
from haversine import haversine # Imported this library so that I can use the distance formula for lat/long

# CONSTANTS to access ipinfo.io API
access_token = 'a501254463d445'
handler = ipinfo.getHandler(access_token)

# CONSTANT- store of current IP addresses as a dictionary
# key- IP address
# value- relevant information stored as a tuple
# gets rid of repeated IP addresses
locations = {}
with open("IP.txt") as f:
    content = f.read().splitlines()

    for i in content:
        type = i.split(" ")[0]
        ip_address = i.split(" ")[1]
        details = handler.getDetails(ip_address)
        latitude = details.latitude
        longitude = details.longitude

        # only stores IP address if it's unique
        if locations.get(ip_address) == None:
            locations[ip_address] = (ip_address, type, latitude, longitude)


# gets the score of the inputted IP address
def getScore( ipAddress ):
    details = handler.getDetails(ipAddress)

    newLocation = (ipAddress, details.latitude, details.longitude)

    closest_login = ("ip", "type", sys.float_info.max)
    currentLoc = (float(newLocation[1]), float(newLocation[2]))
    for i in locations:
        # If it is already registered IP address, score = 0
        if i == ipAddress:
            return "Score: 0"
        # find the closest distance IP
        else:
            otherLoc = (float(locations[i][2]), float(locations[i][3]))
            distance = haversine(currentLoc, otherLoc)
            if closest_login[2] > distance:
                closest_login = (locations[i][0], locations[i][1], distance )

    if closest_login[1] == "FRAUD":
        return "Score: " + str( 2 * closest_login[2] )
    else:
        return "Score: " + str( closest_login[2] )


# Continually checks new IP addresses until you end the program
while( True ):
    IP = input("What IP address do you wish to check?" )
    try:
        print( getScore(IP) )
    except Exception:
        print("Sorry, that IP address is invalid.")







'''
# Checks with other locations
closest_login = {}

# Find the closest location
for i in locations:
    closest_login[i] = ("ip", "type", sys.float_info.max)
    currentLoc = (float(locations[i][2]), float(locations[i][3]))
    # print(currentLoc)
    for j in locations:
        if i != j:
            otherLoc = (float(locations[j][2]), float(locations[j][3]))
            distance = haversine(currentLoc, otherLoc)
            if closest_login[i][2] > distance:
                closest_login[i] = (locations[i][0], locations[i][1], distance )

for i in closest_login:
    printStr = "IP addres: " + i + "\nType: " + locations[i][1] + "\nClosest Location Type: " + closest_login[i][1]
    if closest_login[i][1] == "FRAUD":
        printStr = printStr + "\nScore: " + str(closest_login[i][2] )#* 2)
    else:
        printStr = printStr + "\nScore: " + str(closest_login[i][2])
    print( printStr)
    print()
'''
