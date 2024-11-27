from random import randrange
from collections import Counter
import sys
from helpers import get_input
from api import get_posts, get_comments, post_comment, get_all_comments

def view_posts_menu():
    print("Choose an option:")
    print("1. View 10 random post titles")
    print("2. View 10 most commented post titles")
    print("3. exit")
    value = get_input(3)
    if value == 1:
        view_random_posts()
    if value == 2:
        view_top_posts()
    if value == 3:
        sys.exit(0)

    return

def view_post_menu():
    pass
        

def view_comments_menu():
    pass

def view_random_posts():
    posts = get_posts()
    post_count = len(posts)
    for i in range(10):
        rand_int = randrange(0,post_count-1)
        print(f"[Post] {posts[rand_int]["title"]}")
        print(posts[rand_int]["body"])

    view_post_menu()

def view_top_posts():
    posts = get_posts()
    comments = get_all_comments()
    post_ids = [comment['postId'] for comment in comments]
    top_ids = sorted(set(post_ids))
    for i in range(10):
        print(f"[Post] {posts[top_ids[i]]["title"]}")
        print(posts[top_ids[i]]["body"])

def view_comments():
    pass


print("Blog Viewer")
while True:
    view_posts_menu()
