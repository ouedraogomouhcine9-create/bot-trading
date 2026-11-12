import json
import os
import urllib.parse
import urllib.request

url = "https://query1.finance.yahoo.com/v8/finance/chart/GBPJPY=X"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=20) as r:
    data = json.load(r)
prix = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
print("Prix GBPJPY :", prix)


def envoyer(texte):
    token = os.environ["TELEGRAM_TOKEN"]
    chat = os.environ["TELEGRAM_CHAT_ID"]
    api = f"https://api.telegram.org/bot{token}/sendMessage"
    corps = urllib.parse.urlencode({"chat_id": chat, "text": texte}).encode()
    urllib.request.urlopen(api, data=corps, timeout=20)


if os.environ.get("GITHUB_EVENT_NAME") == "workflow_dispatch":
    envoyer(f"Test OK. Prix GBPJPY : {prix}")
