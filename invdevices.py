import meraki
import json

api_key ='6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
dashboard = meraki.DashboardAPI(api_key)
organization_id = '566327653141842188'


def devicedata(device_input):
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
devicesdata = dashboard.organizations.getOrganizationInventoryDevices(organization_id)
devices_data = devicedata(devicesdata)
pretty_response = json.dumps(devices_data,indent = 4)
filename = 'invdevicedata.txt'
with open (filename, 'w') as file :
    file.write(pretty_response)
    print('saved to file')
    file.close() 