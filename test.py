import requests

base = "http://127.0.0.1:5000/"

response = requests.patch(base + "video/2", {"views": 99, "likes": 101})
print(response.json())
