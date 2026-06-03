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
    url = "https://geocode.maps.co/search?q=" + urllib.parse.quote(addr)
    # Geocode.maps.co is free and often doesn't need API key for low usage, but it may require it now.
    # Let's try nominatim again but carefully.
    n_url = "https://nominatim.openstreetmap.org/search?q=" + urllib.parse.quote(addr) + "&format=json"
    req = urllib.request.Request(n_url, headers={'User-Agent': 'AntigravityDataTool/1.0 (test@example.com)'})
    try:
        resp = urllib.request.urlopen(req)
        data = json.loads(resp.read())
        if data:
            results[addr] = (data[0]['lat'], data[0]['lon'])
            print(f"Found {addr}: {data[0]['lat']}, {data[0]['lon']}")
        else:
            # try without NY zip
            n_url2 = "https://nominatim.openstreetmap.org/search?q=" + urllib.parse.quote(addr.split(", NY")[0] + ", Queens, NY") + "&format=json"
            req2 = urllib.request.Request(n_url2, headers={'User-Agent': 'AntigravityDataTool/1.0 (test@example.com)'})
            try:
                resp2 = urllib.request.urlopen(req2)
                data2 = json.loads(resp2.read())
                if data2:
                    results[addr] = (data2[0]['lat'], data2[0]['lon'])
                    print(f"Found {addr}: {data2[0]['lat']}, {data2[0]['lon']}")
                else:
                    print(f"Not found: {addr}")
            except Exception as e:
                print(f"Error 2 on {addr}: {e}")
    except Exception as e:
        print(f"Error on {addr}: {e}")
    time.sleep(2)

print("Done")
