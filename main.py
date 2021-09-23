from flask import Flask, render_template, request
import pyautogui
import qrcode
import logging
import socket
import random


app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
pyautogui.FAILSAFE = False

NAME = socket.gethostname()
REFERENCE = random.randint(1111,9999)
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = str(s.getsockname()[0])
    s.close()
    return ip
# "/" + str(REFERENCE) + 

@app.route("/")
def home():
    ip = get_ip()
    return render_template('index.html', ip=ip, reference=REFERENCE)

@app.route("/increaseSound", methods=['GET', 'POST'])
@app.route("/decreaseSound", methods=['GET', 'POST'])
@app.route("/muteSound", methods=['GET', 'POST'])
def changeSound():
    command = request.path
    if 'increase' in command:
        pyautogui.press("up")
    elif 'decrease' in command:
        pyautogui.press("down")
    elif 'mute' in command:
        pyautogui.press("volumemute")
    return render_template('index.html')

@app.route( "/moveFoward", methods=['GET', 'POST'])
@app.route("/moveBack", methods=['GET', 'POST']) 
def seek():
    command = request.path
    if 'Foward' in command:
        pyautogui.press("left")
    if 'Back' in command:
        pyautogui.press("right")

    return render_template('index.html')

@app.route("/cmndQbutton", methods=['GET', 'POST'])
def cmndQ():
    command = request.path
    if 'cmnd' in command:
        pyautogui.hotkey("command", "q")
    return render_template('index.html')


@app.route("/playpause", methods=['GET', 'POST'])
def playpause():
    command = request.path
    if 'play' in command:
        pyautogui.press("enter")
    return render_template('index.html')

if __name__ == '__main__':
    

    host = get_ip()+':5000/'
    print('Access at ' + host)

    img = qrcode.make(host)
    # img.show()
    app.run(debug=True, host="0.0.0.0")

