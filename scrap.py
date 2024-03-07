from reddit_bot import reddit_instance
import praw
import pandas as pd

def Scrape(subreddit='stocks'):

    subreddit = reddit_instance.subreddit("IndianStockMarket")
    print(subreddit)

    top_25_sub = subreddit.top(time_filter='week')
    data = []
    for sub in top_25_sub:
        print(sub.title)
        print(sub.selftext)
        sub
        data.append([sub.title, sub.selftext])
        # sub.comment_sort = "confidence"  #
    dataset = Save_csv(data)
    return dataset , data

    

def Save_csv(data = []):
    dataset = pd.DataFrame(data, columns=['Title', 'Content'])
    dataset.to_csv("data.csv", index=False)

    return dataset