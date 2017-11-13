new_rfr = RandomForestRegressor(max_depth=10, max_features='sqrt', n_estimators=20, random_state=0)
new_rfr.fit(X_train, y_train)
y_pred = new_rfr.predict(X_test)

print(metrics.mean_squared_log_error(y_test, y_pred))

kaggle_pred = new_rfr.predict(test_df)
plt.scatter(X_train['GrLivArea'], y_train, c='blue', alpha=0.5)
plt.scatter(X_test['GrLivArea'], y_pred, c='green')
plt.scatter(test_df['GrLivArea'], kaggle_pred, c='red')

new_rfr_output = np.vstack((test_ids, kaggle_pred)).T
submission = pd.DataFrame(new_rfr_output, columns=['Id', 'SalePrice'])
submission.Id = submission.Id.astype(np.int)
submission.to_csv('../data/tuned_rfr_output_submission.csv', index=False)
