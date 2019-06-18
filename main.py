import requests, json

# API_KEY of account, please refer API Key tab after login via browser
API_KEY = "O8vxLvd8ri_UTRFimWwRiwzC3WiXVhItyFPmHJ33jTWcZxN-71Iz8wgCHs1x5V6hchJTrDEyZTgJU5xI1pYnIA"

# Comma Separated list of IPs of devices for which connection to DNS should be allowed
# Number of IPs in list should NOT exceed total number of IPs allowed under your account.
ip_list = '100.0.0.1,100.0.0.2'

# Header contains API KEY
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'x-runtime': '148ms',
    'apikey' : API_KEY
    }

#URL to request the update in list of IPs
url = 'https://accounts.seclookup.com/ip-list'
payload = { 'ip_list': ip_list}
response = requests.post(url, allow_redirects=True, headers=headers, data=payload)
print("add_ips", response.content, response.status_code)

