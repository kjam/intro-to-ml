y = tweet_df.author
X_train, X_test, y_train, y_test = train_test_split(tweet_df['status'], y, test_size=0.33, random_state=53)
