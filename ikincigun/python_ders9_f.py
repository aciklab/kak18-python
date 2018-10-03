#!/usr/bin/python3

from flask import Flask
 
 
import webview
import sys
import threading
 
app = Flask(__name__)
 
 
@app.route('/')
def hello_world():
    return 'Hello to the World!'
 
def start_server():
    app.run()
 
if __name__ == '__main__':
    """  https://github.com/r0x0r/pywebview/blob/master/examples/http_server.py
    """
 
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
 
    webview.create_window("It works, Joe!", "http://127.0.0.1:5000/")
 
    sys.exit()
