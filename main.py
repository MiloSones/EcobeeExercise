from random import randrange
from collections import Counter
import sys
from helpers import get_input
from api import get_posts, get_posts_comments, post_comment, get_all_comments

def view_posts_menu():
    print("Choose an option:")
    print("1. View 10 random post titles")
    print("2. View 10 most commented post titles")
    print("3. exit")
    value = -1
    while(value == -1):
        value = get_input(3)
        if value == 1:
            view_random_posts()
        if value == 2:
            view_top_posts()
        if value == 3:
            sys.exit(0)

    return

def view_post_menu(posts):
    print("Choose an option:")
    print("1.View post content")
    print("2. Back to post explorer")
    value = -1
    while(value == -1):
        value = get_input(1)
        if value == 11:
            view_posts_menu()
        print(f"[Post] {posts[value]["title"]}\n")
        print(f"{posts[value]["body"]}")
    return

def view_comments_menu():
    pass

def view_random_posts():
    posts = get_posts()
    post_count = len(posts)
    random_posts = []
    for i in range(10):
        rand_int = randrange(0,post_count-1)
        random_posts.append(posts[rand_int])
        print(f"[{i+1}] {random_posts[i]}")
        
    view_post_menu(random_posts)

def view_top_posts():
    posts = get_posts()
    comments = get_all_comments()
    post_ids = [comment['postId'] for comment in comments]
    top_ids = sorted(set(post_ids))
    for i in range(10):
        print(f"[{i+1}] {posts[top_ids[i]]["title"]}")



def view_comments():
    pass


print("Blog Viewer")
while True:
    view_posts_menu()
