import requests

url = "https://dantri.com.vn/suc-khoe.htm"
response = requests.get(url)
print(response.content.decode())

