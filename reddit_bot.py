import praw



reddit_instance = praw.Reddit(
    client_id = client_id,
    client_secret = client_secret,
    username = username,
    password = password,
    
    user_agent = 'test_bot'
)

# print(reddit_instance.user.me())
