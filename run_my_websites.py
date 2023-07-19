import requests
from datetime import datetime
import time


while True:

    print(str(datetime.now()).split()[1][:5])

    requests.get("https://personal-site-5659.onrender.com/")
    requests.get("https://bugtk.azurewebsites.net/")

    time.sleep(720)
