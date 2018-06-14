import _tkinter
import pip
package_name='tweepy'
pip.main(['install', package_name])


consumer_key = 'your consumer key'
consumer_secret = 'your consumer secret key'
access_token = 'your access token'
access_token_secret = 'your access secret token'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def doWork():
    search = "keyword"

    numberOfTweets = "100"

    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweet.favorite()
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

root = Tk()

label1 = Label(root, text="Search")
E1 = Entry(root, bd=5)

label2 = Label(root, text="Number of Tweets")
E2 = Entry(root, bd=5)

label3 = Label(root, text="Favorite")
E3 = Entry(root, bd=5)

label1.pack()
E1.pack()

label2.pack()
E2.pack()

label3.pack()
E3.pack()

root.mainloop()