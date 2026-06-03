import urllib.request
import json
import urllib.parse
import time

addresses = [
    "37-12 Main St, Flushing, NY 11354",
    "136-21 Roosevelt Ave, Flushing, NY 11354",
    "40-52 Main St, Flushing, NY 11354",
    "37-11 Main St, Flushing, NY 11354",
    "41-28 Main St, Flushing, NY 11355",
    "41-10 Main St, Flushing, NY 11355",
    "135-45 Roosevelt Ave, Flushing, NY 11354",
    "39-16 Main St, Flushing, NY 11354",
    "135-26 Roosevelt Ave, Flushing, NY 11354",
    "134-16 36th Road, Flushing, NY 11354",
    "136-11 38th Ave, Flushing, NY 11354",
    "36-20 Union St, Flushing, NY 11354"
]

results = {}
for addr in addresses:
    url = "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/findAddressCandidates?f=json&singleLine=" + urllib.parse.quote(addr)
    req = urllib.request.Request(url)
    try:
        resp = urllib.request.urlopen(req)
        data = json.loads(resp.read())
        if 'candidates' in data and len(data['candidates']) > 0:
            loc = data['candidates'][0]['location']
            print(f"Found {addr}: {loc['y']}, {loc['x']}")
        else:
            print(f"Not found: {addr}")
    except Exception as e:
        print(f"Error on {addr}: {e}")
    time.sleep(0.5)

print("Done")
