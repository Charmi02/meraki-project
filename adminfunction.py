
import requests
import json
api_key ="6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
org_id ="566327653141842188"

headers = {
        "Content-Type": "application/json",
        "X-Cisco-Meraki-API-Key": api_key,
    }

url = f"https://api.meraki.com/api/v1/organizations/{org_id}/admins"
response = requests.get(url, headers=headers)

def pulladmindata(admin_input):
  
    admins = []
    i = 0
    for admin in admin_input:
        admin = {}
        admin['name'] = admin_input[i]['name']
        admin['email'] = admin_input[i]['email']
        admin['orgAccess'] = admin_input[i]['orgAccess']
        admin['lastActive'] = admin_input[i]['lastActive']
        i += 1
        admins.append(admin)
    return admins

if response.status_code == requests.codes.ok:
    admins = response.json()
    admins_data = pulladmindata(admins)
    pretty_response = json.dumps(admins_data,indent=4)
    filename ='admin.txt'
    with open (filename, 'w') as file:
        #write the data into the file
        file.write(pretty_response)
        print('saved to file')
        file.close()

