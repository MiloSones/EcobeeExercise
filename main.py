import random
import sys
from helpers import get_input
from api import get_posts, get_comments, post_comment

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
    pass

def view_top_posts():
    pass

def view_comments():
    pass


print("Blog Viewer")
while True:
    view_posts_menu()
    