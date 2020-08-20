#random joke generator
import praw
import random
from tkinter import *

root = Tk()


def random_joke():
    reddit = praw.Reddit(client_id = 'enter id here',client_secret = 'enter password here', user_agent = 'Kyle' )
    jokes_list = []
    jokes = reddit.subreddit('Oneliners').hot(limit=100)
    for post in jokes:
        jokes_list.append(post.title)
    
    answer = random.choice(jokes_list)
    label = Label(text = answer)
    label.pack()

myButton = Button(text = 'Random Joke', command = random_joke)
myButton.pack()

q = input('Enter q to quit')

root.mainloop()

