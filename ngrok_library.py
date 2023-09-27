import atexit
import json
import os
import platform
import shutil
import subprocess
import tempfile
import time
import zipfile
from pathlib import Path
from threading import Timer
from waitress import serve
import requests


def disable_clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('setterm -cursor off')
def _run_ngrok(port,token,domain):

    ngrok_path = str(Path(tempfile.gettempdir(), "ngrok"))
    _download_ngrok(ngrok_path)
    
    system = platform.system()
    if system == "Darwin":
        command = "ngrok"
    elif system == "Windows":
        command = "ngrok.exe"
    elif system == "Linux":
        command = "ngrok"
    else:
        raise Exception(f"{system} is not supported")
    executable = str(Path(ngrok_path, command))
    os.chmod(executable, 777)
    #disable_clear()
    ngrok = ""
    if token != None:
     print("token set")
     t = subprocess.Popen([executable,'config', "add-authtoken",token])
     time.sleep(1)
     t.kill()

    time.sleep(5)
    if domain != None:
     ngrok = subprocess.Popen([executable,'http',f"--domain={domain}", str(port)])
    else:
     ngrok = subprocess.Popen([executable,'http', str(port)]) 
    time.sleep(1)
    print(port)
    atexit.register(ngrok.terminate)
    localhost_url = "http://localhost:4040/api/tunnels"  # Url with tunnel details
    time.sleep(1)
    tunnel_url = requests.get(localhost_url).text  # Get the tunnel information
    j = json.loads(tunnel_url)
    

    tunnel_url = j['tunnels'][0]['public_url']  # Do the parsing of the get
    tunnel_url = tunnel_url.replace("https", "http")
    return tunnel_url


def _download_ngrok(ngrok_path):
    if not Path(ngrok_path).exists():
        print(f"ngrok not exist in temp {ngrok_path}")
        quit()
   




def start_ngrok(port,token,domain):
    print(port,token,domain)
    ngrok_address = _run_ngrok(port,token,domain)
    print(f" * Running on {ngrok_address}")
    print(f" * Traffic stats available on http://127.0.0.1:{port}")


def run_with_ngrok(app):
    """
    The provided Flask app will be securely exposed to the public internet via ngrok when run,
    and the its ngrok address will be printed to stdout
    :param app: a Flask application object
    :return: None
    """
    
    #old_run = app.run
    print("Run with ngrok")
    def new_run(port = 5000,token = None,domain = None):
        thread = Timer(1, start_ngrok,args=(port,token,domain,))
        thread.setDaemon(True)
        thread.start()
        serve(app,port = port)
        #old_run()
    app.run = new_run