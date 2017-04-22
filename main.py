import json, requests

def getSecret(service, token='null'):

    with open("secrets.json") as data:
        s = json.load(data)
        #print s
        #print s['{}'.format(service)]['{}'.format(token)]
        # If there is no token, return whole parent object
        if token == 'null':
            secret = s['{}'.format(service)]
        else:
            secret = s['{}'.format(service)]['{}'.format(token)]
        return secret

mytoken = getSecret("token")
cid = getSecret("client")
csec = getSecret("secret")
ruri = 'rdenton.local:5000/authorization'

headers = {"Authorization": "Bearer {}".format(mytoken)}
athlete = "https://www.strava.com/api/v3/athlete/activities"
payload = {"per_page": 2}
r = requests.get(athlete,headers=headers)
rjson = json.dumps(r.json(), sort_keys=True, indent=4, separators=(',',': '))
print(rjson)
