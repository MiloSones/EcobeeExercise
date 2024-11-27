import requests

BASE_URL = "https://jsonplaceholder.typicode.com/"
TIMEOUT = 10

def get_posts():
    try:
        r = requests.get(BASE_URL + "posts", timeout=TIMEOUT)
        if r.status_code == 200:
            return r.json()
        else:
            print(f"Status code: {r.status_code}")
            return 0
    except requests.exceptions.Timeout:
        print("Timed out")

def get_comments(post_id):
    try:
        r = requests.get(BASE_URL + f"comments/{post_id}", timeout=TIMEOUT)
        if r.status_code == 200:
            return r.json()
        else:
            print(f"Status code: {r.status_code}")
            return 0
    except requests.exceptions.Timeout:
        print("Timed out")

def post_comment(comment):
    return 0