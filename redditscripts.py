import praw

reddit = praw.reddit(clienId = '',
                    clientSecret = '',
                    username='',
                    password='',
                    userAgent='')

subreddit = reddit.subreddit('')
#buildapcsales

newPython = subreddit.new(limit=5)

for submission in newPython:
    print(submission)
