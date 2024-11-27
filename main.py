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
    print("1-10. View post content")
    print("11. Back to post explorer")
    value = -1
    while(value == -1):
        value = get_input(11)
        if value == 11:
            view_posts_menu()
        if 1 <= value <= 10:
            print(f"[Post] {posts[value-1]["title"]}\n")
            print(f"{posts[value-1]["body"]}\n")
    view_comments_menu(value)

def view_comments_menu(post_id):
    print("Choose an option:")
    print("1. View comments")
    print("2. Add comment")
    print("3. Back to post explorer")
    value = -1
    while(value == -1):
        value = get_input(3)
        if value == 1:
            view_comments(post_id)
        if value == 2:
            add_comment(post_id)
        if value ==3:
            view_posts_menu()
    return

def view_random_posts():
    posts = get_posts()
    post_count = len(posts)
    random_posts = []
    for i in range(10):
        rand_int = randrange(0,post_count-1)
        random_posts.append(posts[rand_int])
        print(f"[{i+1}] {random_posts[i]["title"]}")
        
    view_post_menu(random_posts)

def view_top_posts():
    posts = get_posts()
    comments = get_all_comments()
    top_posts = []
    post_ids = [comment['postId'] for comment in comments]
    top_ids = sorted(set(post_ids))
    for i in range(10):
        top_posts.append(posts[top_ids[i]])
        print(f"[{i+1}] {top_posts[i]["title"]}")

    view_post_menu(top_posts)


def view_comments(post_id):
    post_comments = get_posts_comments(post_id)
    for comment in post_comments:
        print(f"[{comment["email"]}] {comment["name"]}\n")
        print(f"{comment["body"]}\n")


def add_comment(post_id):
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    body = input("Write your comment: ")

    comment = {
        "name": name,
        "emai": email,
        "body": body,
    }

    if post_comment(post_id, comment) == 201:
        print("Succefully added comment\n")
    else:
        print("Something went wrong!")


print("Blog Viewer")
while True:
    view_posts_menu()
