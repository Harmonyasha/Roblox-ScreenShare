import time
from PIL import ImageGrab, ImageOps
from flask import Flask, jsonify, request, render_template
import ngrok_library
app = Flask(__name__,static_url_path='') #/cool2
ngrok_library.run_with_ngrok(app)
@app.route('/', methods=['POST'])
def result():
    if "getimg" in request.json:
        t = time.time()
        sizes = open("monitor_size.txt","r")
        sizes = sizes.readline()
        sizes = sizes.split("x")
        snapshot = ImageGrab.grab()
        snapshot = snapshot.resize((int(sizes[0]),int(sizes[1])))
        snapshot = ImageOps.mirror(snapshot)
        pixels = snapshot.load()
        width, height = snapshot.size
        all_pixels = []
        all_pixels.append(f"video;{str(width)}x{str(height)};")
        for x in range(width):
            for y in range(height):
                cpixel = pixels[x, y]
                cpixel = str(cpixel)
                cpixel = cpixel.replace("(","").replace(")","")
                all_pixels.append(cpixel+";")
        snapshot.close()
        print(f"sended for {time.time()-t}")
        return ''.join(str(x) for x in all_pixels)
    return "Invalid method"


if __name__ == "__main__":
  app.run(token = "YourNgrokToken",domain = "Create domain if you want")

    
