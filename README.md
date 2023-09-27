
Python script for share your screen to roblox
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
# Setup
Change inside the script this
```py
 app.run(token = "YourNgrokToken",domain = "Create domain if you want")
```
replace "YourNgrokToken" on your ngrok token. You can get it here 
```c
https://dashboard.ngrok.com/get-started/setup
```
You can remove domain but if you wanna keep it create your domain and replace "Create domain if you want" on your domain
```c
https://dashboard.ngrok.com/cloud-edge/domains
```

# To run you should
execute require in developer console or in serverside executor
```lua
require(11643001589)("RobloxUserName","NgrokUrl")
```
