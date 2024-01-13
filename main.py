import time
from PIL import ImageGrab, ImageOps
from flask import Flask, jsonify, request, render_template
import ngrok_library
import threading
arr = {}
frame = 20
app = Flask(__name__,static_url_path='')
ngrok_library.run_with_ngrok(app)


def recordimage():
    global arr
    position = arr.__len__()
    arr[position] = "nil"
    t = time.time()
    sizes = open("monitor_size.txt","r")
    sizes = sizes.readline()
    sizes = sizes.split("x")
    snapshot = ImageGrab.grab()
    snapshot = snapshot.resize((int(sizes[0]),int(sizes[1])))
    snapshot = ImageOps.mirror(snapshot)
    pixels = snapshot.load()
    width, height = snapshot.size
    snapshot.close()
    all_pixels = []
    all_pixels.append(f"video;{str(width)}x{str(height)};")
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            cpixel = str(cpixel)
            cpixel = cpixel.replace("(","").replace(")","")
            all_pixels.append(cpixel+";")

    arr[position] = (''.join(str(x) for x in all_pixels).replace(" ",""))
    

def check():
    ret = True
    try:
        for v in arr:
            if arr[v] == "nil":
                ret = False
    except: 
        ret = False
    return ret

@app.route('/', methods=['POST'])
def result():
    global arr 
    #while not check():
    #    None
    clonearr = arr
    arr = {}
    return clonearr

@app.route('/reset', methods=['POST'])
def reset():
    global arr 
    arr = {}
    return "True"

def flaskrun():
    app.run(token = "YourNgrokToken",domain = "Create domain if you want")

th = threading.Thread(target=flaskrun)
th.start()


while True:
        threading.Thread(target=recordimage).start()
        time.sleep(.1)