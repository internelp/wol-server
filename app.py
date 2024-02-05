import os

from flask import Flask, render_template, request
from wakeonlan import send_magic_packet

app = Flask(__name__)


@app.route('/')
def main():  # put application's code here
    return render_template('index.html')


@app.route('/do-wol', methods=["get"])
def do_wol():
    mac_addr = request.args.get("mac")
    try:
        send_magic_packet(mac_addr)
        resp = "Broadcast sent, please wait for the device to wake up."
    except Exception as e:
        resp = e
    return str(resp)


if __name__ == '__main__':
    app.run('0.0.0.0')
