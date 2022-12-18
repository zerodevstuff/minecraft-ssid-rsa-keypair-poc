import requests
ssid = input('ssid:')
url = ("https://api.minecraftservices.com/player/certificates")
headers = {
    'Authorization': f"Bearer {ssid}",
    'Content-Type': 'application/json',
}
resp = requests.post(url, headers=headers)
print(resp.status_code)
print(resp.text)