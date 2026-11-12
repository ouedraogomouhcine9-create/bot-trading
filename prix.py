import json
import urllib.request

url = "https://query1.finance.yahoo.com/v8/finance/chart/GBPJPY=X"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

with urllib.request.urlopen(req, timeout=20) as r:
    data = json.load(r)

prix = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
print("Prix GBPJPY :", prix)
