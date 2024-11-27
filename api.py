import requests

BASE_URL = "https://jsonplaceholder.typicode.com/"
TIMEOUT = 5

def get_posts():
    try:
        r = requests.get(BASE_URL + "posts/", timeout=TIMEOUT)
        if r.status_code == 200:
            return r.json()

        print(f"Status code: {r.status_code}")
        return 0
    except requests.exceptions.Timeout:
        print("Timed out")

def get_posts_comments(post_id):
    try:
        r = requests.get(BASE_URL + f"posts/{post_id}/comments", timeout=TIMEOUT)
        if r.status_code == 200:
            return r.json()

        print(f"Status code: {r.status_code}")
        return 0
    except requests.exceptions.Timeout:
        print("Timed out")

def get_all_comments(post_id):
    try:
        r = requests.get(BASE_URL + "comments", timeout=TIMEOUT)
        if r.status_code == 200:
            return r.json()

        print(f"Status code: {r.status_code}")
        return 0
    except requests.exceptions.Timeout:
        print("Timed out")

def post_comment(post_id,comment):
    try:
        r = requests.post(BASE_URL + f"posts/{post_id}/comments",json=comment, timeout=TIMEOUT)
        return r.status_code
    except requests.exceptions.Timeout:
        print("Timed out")