import requests

r = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")

print(r.json()[:2])