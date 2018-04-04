#####################################
# Prime Infrastructure 3 Querier v1 #
# --------------------------------- #
#  Usage:                           #
#  $ python3 pi3q.py                #
#    -u <user> -p <pass>: from PI   #
#    -l: lists all devices          #
#    -s: search                     #
#        -f <field> -v <value>      #
#    -r: show in raw mode (json)    #
# - - - - - - - - - - - - - - - - - #
#    where <field>:                 #
#           ipAddress               #
#           deviceName              #
#           deviceType              #
# --------------------------------- #
# Daniel Urgell: durgell@cisco.com  #
#        Cisco Systems 2018         #
#####################################


import requests
import json
import argparse
import base64

def get_args():
    parser = argparse.ArgumentParser(description='Prime Infrastructure 3 Querier v1')
    parser.add_argument('-u', '--username', type=str, help='set username')
    parser.add_argument('-p', '--password', type=str, help='set password')
    parser.add_argument('-r', '--raw', help='list raw inventory in json format', action='store_true')
    parser.add_argument('-l', '--listdevices', help='list devices', action='store_true')
    parser.add_argument('-s', '--search', help='search devices by field', action='store_true')
    parser.add_argument('-f', '--field', type=str, choices=['ipAddress', 'deviceName', 'deviceType'], help='set field as search filter')
    parser.add_argument('-v', '--value', type=str, help='set value to search')
    args = parser.parse_args()
    return args

def get_from_pi(api, username, password):
    #REMEMBER TO CHANGE THE HOST AND DOMAIN IN THE URL BELOW
    pi3_base = 'https://primeinfra3.corporate.com/webacs/api/v3/data'
    address = pi3_base + api
    credentials = username + ':' + password
    b64_cred = base64.b64encode(credentials.encode('utf-8')) 
    str_b64_cred = b64_cred.decode('utf-8')
    header = {'authorization': 'Basic ' + str_b64_cred, 'content-type': 'application/json'}
    r = requests.get(address, headers=header)
    return r

def search_devices_by_field(username, password, field, value):   
    if field == 'ipAddress' and value!=None:
        api='/Devices.json?ipAddress=contains%28%22' + value + '%22%29'
    elif field == 'deviceName' and value!=None:
        api='/Devices.json?deviceName=contains%28%22' + value + '%22%29'
    elif field == 'deviceType' and value!=None:
        api='/Devices.json?deviceType=contains%28%22' + value + '%22%29'
    else:
        api=None
    
    if api!=None:
        r=get_from_pi(api, username, password)
        return r

def print_device(device_data):
    if 'deviceName' in device_data['queryResponse']['entity'][0]['inventoryDetailsDTO']['summary']:
        print('deviceName: ' + device_data['queryResponse']['entity'][0]['inventoryDetailsDTO']['summary']['deviceName'])
    else:
        print('deviceName: unknown')
        
    if 'deviceType' in device_data['queryResponse']['entity'][0]['inventoryDetailsDTO']['summary']:
        print('deviceType: ' + device_data['queryResponse']['entity'][0]['inventoryDetailsDTO']['summary']['deviceType'])
    else:
        print('deviceType: unknown')
    
    if 'ipAddress' in device_data['queryResponse']['entity'][0]['inventoryDetailsDTO']['summary']:
       print('ipAddress: ' + device_data['queryResponse']['entity'][0]['inventoryDetailsDTO']['summary']['ipAddress'])
    else:
        print('ipAddress: unknown')
    
    if 'softwareVersion' in device_data['queryResponse']['entity'][0]['inventoryDetailsDTO']['summary']:
        print('softwareVersion: ' + device_data['queryResponse']['entity'][0]['inventoryDetailsDTO']['summary']['softwareVersion'])
    else:
        print('softwareVersion: unknown')
    
    print('')

def print_devices(username, password, devices_data):
    if 'entityId' in devices_data['queryResponse']:
        for entityId in devices_data['queryResponse']['entityId']:
            api= '/InventoryDetails/' + entityId['$'] + '.json'
            r = get_from_pi(api, username, password)
            print_device(r.json())

def print_raw_inventory(inventory_data):
    print (json.dumps(inventory_data, indent=4, sort_keys=True))


def print_raw_inventory_verbose(username, password, devices_data):
    for entityId in devices_data['queryResponse']['entityId']:
        api= '/InventoryDetails/' + entityId['$'] + '.json'
        r = get_from_pi(api, username, password)
        print_raw_inventory(r.json())

args = get_args()
if args.username != None and args.password != None:
    username = args.username
    password = args.password

    if args.listdevices:
        #list all devices
        api = '/InventoryDetails.json'
        r = get_from_pi(api, username, password)
        if args.raw:
            print_raw_inventory_verbose(username, password, r.json())
        else:
            print_devices(username, password, r.json())

    elif args.search:
        #list all devices by field/value match
        if args.field!=None and args.value!=None:
            r=search_devices_by_field(username, password, args.field, args.value)
            if args.raw:
                print_raw_inventory_verbose(username, password, r.json())
            else:
                print_devices(username, password, r.json())
        else:
            print('Error: must set field and value to search!')
    else:
        print('Error: Wrong options!')

else:
    print('Error: Must provide credentials!')

 