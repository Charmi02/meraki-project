
import requests
import json
api_key ="6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
org_id ="566327653141842188"

headers = {
        "Content-Type": "application/json",
        "X-Cisco-Meraki-API-Key": api_key,
    }

url = f"https://api.meraki.com/api/v1/organizations/{org_id}/inventoryDevices"
response = requests.get(url, headers=headers)

def pullDevicedata(device_input):
  
    devices = []
    i = 0
    for device in device_input:
        device = {}
        device['mac'] = device_input[i]['mac']
        device['serial'] = device_input[i]['serial']
        device['networkId'] = device_input[i]['networkId']
        device['productType'] = device_input[i]['productType']
        i += 1
        devices.append(device)
    return devices

if response.status_code == requests.codes.ok:
    devicesdata = response.json()
    devices_data = pullDevicedata(devicesdata)
    pretty_response = json.dumps(devices_data,indent=4)
    filename ='device.txt'
    with open (filename, 'w') as file:
        #write the data into the file
        file.write(pretty_response)
        print('saved to file')
        file.close()

