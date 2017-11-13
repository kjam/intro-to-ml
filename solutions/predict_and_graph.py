kaggle_pred = svr.predict(test_df)

plt.scatter(X_train['GrLivArea'], y_train, c='blue', alpha=0.5)
plt.scatter(X_test['GrLivArea'], y_pred, c='green')
plt.scatter(test_df['GrLivArea'], kaggle_pred, c='red')
