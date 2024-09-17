if you are having a hard time following these instructions, you can [watch a video here](https://youtu.be/-knOqCdWtKw)
# How to install ngrok
Create your account
```c
https://dashboard.ngrok.com/signup
```
Download ngrok
```c
https://ngrok.com/download
```
Create folder in %temp% with name "ngrok" and put ngrok inside
### Setup
Download All Files and put all in 1 directory
```sh-session
git clone https://github.com/Harmonyasha/Roblox-ScreenShare.git
cd Roblox-ScreenShare
pip install -r requirements.txt
```
or
```sh-session
pip install -r requirements.txt
```

Change inside the script this line
```py
 app.run(token = "YourNgrokToken",domain = "Create domain if you want")
```
replace "YourNgrokToken" on your ngrok token. You can get it here 
```c
https://dashboard.ngrok.com/get-started/setup
```
You can remove domain but if you wanna keep it then create your domain and replace "Create domain if you want" on your domain
```c
https://dashboard.ngrok.com/cloud-edge/domains
```

### To run you should
execute require in developer console or in serverside executor
```lua
require(15681840577)("RobloxUserName","NgrokUrl")
```
