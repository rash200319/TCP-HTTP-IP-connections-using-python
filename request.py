import requests 
r=requests.get("https://uom.lk")
#https://httpbin.org/get
#https://www.google.com/search?q=python
print(r.status_code)
print(r.url)
print(r.text)
