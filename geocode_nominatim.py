import urllib.request
import json
import urllib.parse
import time

addresses = [
    "143-09 Holly Ave, Flushing, NY 11355",
    "136-20 Booth Memorial Ave, Flushing, NY 11355",
    "37-12 Main St, Flushing, NY 11354",
    "136-21 Roosevelt Ave, Flushing, NY 11354",
    "41-10 Main St, Flushing, NY 11355",
    "135-45 Roosevelt Ave, Flushing, NY 11354",
    "40-52 Main St, Flushing, NY 11354",
    "39-16 Main St, Flushing, NY 11354"
]

results = []
for addr in addresses:
    url = "https://nominatim.openstreetmap.org/search?q=" + urllib.parse.quote(addr) + "&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'AntigravityAgent (contact@example.com)'})
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        if data:
            results.append((addr, data[0]['lat'], data[0]['lon']))
        else:
            # Fallback search
            url2 = "https://nominatim.openstreetmap.org/search?q=" + urllib.parse.quote(addr.split(", NY")[0] + ", Flushing, NY") + "&format=json"
            req2 = urllib.request.Request(url2, headers={'User-Agent': 'AntigravityAgent (contact@example.com)'})
            try:
                response2 = urllib.request.urlopen(req2)
                data2 = json.loads(response2.read())
                if data2:
                    results.append((addr, data2[0]['lat'], data2[0]['lon']))
                else:
                    results.append((addr, "Not found", "Not found"))
            except:
                results.append((addr, "Not found", "Not found"))
    except Exception as e:
        results.append((addr, "Error", str(e)))
    time.sleep(1.2)

for r in results:
    print(f"{r[0]} -> {r[1]}, {r[2]}")
