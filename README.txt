# Prime-Infrastructure-3-Querier
Example of inventory access through REST API

#####################################
# Prime Infrastructure 3 Querier v1 #
# --------------------------------- #
#  Usage:                           #
#  $ python3  pi3q.py               #
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

Examples:
  
$ python3 pi3q.py -u user -p pass -s -f deviceType -v 9396
deviceName: NX9693-2
deviceType: Cisco Nexus 9396PX Switch
ipAddress: 10.0.17.103
softwareVersion: 6.1(2)I2(2a)

deviceName: NX9396-1
deviceType: Cisco Nexus 9396PX Switch
ipAddress: 10.17.3.1
softwareVersion: 6.1(2)I2(2a)

$ python3 pi3q.py -u user -p pass -s -f deviceName -v 9693
deviceName: NX9693-2
deviceType: Cisco Nexus 9396PX Switch
ipAddress: 10.0.17.103
softwareVersion: 6.1(2)I2(2a)

$ python3 pi3q.py -u user -p pass -s -f ipAddress -v 10.17.
deviceName: NX9396-1
deviceType: Cisco Nexus 9396PX Switch
ipAddress: 10.17.3.1
softwareVersion: 6.1(2)I2(2a)

$ python3 pi3q.py -u user -p pass -s -f deviceType -v "Network Analysis Module" -r
{
    "queryResponse": {
        "@requestUrl": "https://primeinfra3.corporate.com/webacs/api/v3/data/InventoryDetails/805143339",
        "@responseType": "getEntity",
        "@rootUrl": "https://primeinfra3.corporate.com/webacs/api/v3/data",
        "@type": "InventoryDetails",
        "entity": [
            {
                "@dtoType": "inventoryDetailsDTO",
                "@type": "InventoryDetails",
                "@url": "https://primeinfra3.corporate.com/webacs/api/v3/data/InventoryDetails/805143339",
                "inventoryDetailsDTO": {
                    "@displayName": "805143339",
                    "@id": 805143339,
                    "cdpNeighbors": {
                        "cdpNeighbor": [
                            {
                                "duplexMode": "FULL_DUPLEX",
                                "farEndInterface": "Ethernet1/8",
                                "interfaceIndex": 1,
                                "nearEndInterface": "MGMT PORT",
                                "neighborCapabilities": "S-4:6",
                                "neighborDeviceName": "xxx-xx-nx5k-a(XXX0000XX0)",
                                "neighborDevicePlatformType": "N5K-C5020P-BF"
                            }
                        ]
                    },
                    "chassis": {
                        "chassis": [
                            {
                                "description": "Cisco Prime Virtual Network Analysis Module ESXi",
                                "entPhysicalIndex": "1",
                                "modelNr": "ESX",
                                "name": "ESX",
                                "productId": "ESX",
                                "serialNr": "XXXXXXXXXXX"
                            }
                        ]
                    },
                    "ethernetInterfaces": {
                        "ethernetInterface": [
                            {
                                "adminStatus": "UP",
                                "description": "DATA PORT",
                                "duplexMode": "AUTO_NEGOTIATE",
                                "macAddress": "00:00:00:00:00:00",
                                "mtu": 1500,
                                "name": "DATA PORT",
                                "operationalStatus": "UP",
                                "speed": 1000000000
                            },
                            {
                                "adminStatus": "UP",
                                "description": "MGMT PORT",
                                "duplexMode": "AUTO_NEGOTIATE",
                                "macAddress": "00:0c:29:00:00:00",
                                "mtu": 1500,
                                "name": "MGMT PORT",
                                "operationalStatus": "UP",
                                "speed": 1000000000
                            }
                        ]
                    },
                    "ipInterfaces": {
                        "ipInterface": [
                            {
                                "adminStatus": "UP",
                                "ipAddress": "192.168.11.11/24",
                                "name": "MGMT PORT",
                                "operationalStatus": "UP"
                            }
                        ]
                    },
                    "physicalPorts": {
                        "physicalPort": [
                            {
                                "description": "MGMT PORT",
                                "equipmentId": 796259487,
                                "name": "MGMT PORT",
                                "residingModule": "ESX",
                                "vendorEquipmentType": "zeroDotZero"
                            },
                            {
                                "description": "DATA PORT",
                                "equipmentId": 796259487,
                                "name": "DATA PORT",
                                "residingModule": "ESX",
                                "vendorEquipmentType": "zeroDotZero"
                            }
                        ]
                    },
                    "summary": {
                        "ciscoIdentityCapable": false,
                        "deviceId": 799446649,
                        "deviceType": "Cisco Prime Virtual Network Analysis Module (ESXi)",
                        "ipAddress": "192.168.11.11",
                        "locationCapable": false,
                        "productFamily": "Cisco Interfaces and Modules",
                        "reachability": "REACHABLE",
                        "softwareVersion": "6.2(1)",
                        "systemTime": "2018-03-29T09:49:43.000Z",
                        "upTime": 19591766455
                    }
                }
            }
        ]
    }
}
