import meraki
import json

api_key ='6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
dashboard = meraki.DashboardAPI(api_key)
organization_id = '566327653141842188'


def admindata(admin_input):
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

admins = dashboard.organizations.getOrganizationAdmins(organization_id)
admins_data = admindata(admins)
pretty_response = json.dumps(admins_data, indent=4)

filename = 'admindata.txt'
with open (filename, 'a') as file :
    file.write(pretty_response)
    print('Saved to file')
    file.close()



