def add_latest_tweets_to_db(author, api, table):
    for tweet in api.user_timeline(author.id, count=200):
        if tweet.author.id == author.id:
            table.insert({'author': author.name,
                          'status': tweet.text})
