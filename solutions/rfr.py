rfr.fit(X_train, y_train)
y_pred = rfr.predict(X_test)
print(metrics.mean_squared_log_error(y_test, y_pred))

kaggle_pred = rfr.predict(test_df)
plt.scatter(X_train['GrLivArea'], y_train, c='blue', alpha=0.5)
plt.scatter(X_test['GrLivArea'], y_pred, c='green')
plt.scatter(test_df['GrLivArea'], kaggle_pred, c='red')
