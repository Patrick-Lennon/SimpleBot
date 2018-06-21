"""
Program to like and/or retweet all the tweets within a certain amount that contain key words
So that I'll never miss an important update or anything else on current events, favorite teams, upcoming games, etc.

# author: Patrick Lennon
"""

from _tkinter import *
import tweepy


consumer_key = 'your info'
consumer_secret = 'your info'
access_token =  'your info'
access_token_secret =  'your info'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


root = Tk()

#making labels for the GUI
label1 = Label(root, text="Search")
E1 = Entry(root, bd=5)

label2 = Label(root, text="Number of Tweets")
E2 = Entry(root, bd=5)

label3 = Label(root, text="Favorite")
E3 = Entry(root, bd=5)

label4 = Label(root, text="Retweeet")
E4 = Entry(root, bd=5)

#Functions returning the text for the boxes in the gui
def getE1():
    return E1.get()

def getE2():
    return E2.get()

def getE3():
    return E3.get()

def getE4():
    return E4.get()

#main function
def doWork():
    getE1()
    search = getE1()

    getE2()
    numberOfTweets = getE2()
    #have to convert the number into an int
    numberOfTweets = int(numberOfTweets)

    getE3()
    fav = getE3()

    getE4()
    re = getE4()


    if fav == "yes" or fav == "Yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                tweet.favorite()
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

    if re == "yes" or re == "Yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                # Retweet
                tweet.retweet()
                print('Retweeted the tweet')

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

#packing each label so it doesn't disappear
label1.pack()
E1.pack()

label2.pack()
E2.pack()

label3.pack()
E3.pack()

label4.pack()
E4.pack()

submit = Button(root, text="Submit", command = doWork)

submit.pack()

root.mainloop()