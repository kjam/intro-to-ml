grid_search = GridSearchCV(estimator=xgbr_base, param_grid=grid_test)
grid_search.fit(X_train, y_train)
scores = grid_search.grid_scores_

top_score = sorted(scores, key=lambda x: x.mean_validation_score, reverse=True)[0]
best_params = top_score.parameters

xgbr = XGBRegressor(learning_rate=0.05, **best_params)
xgbr.fit(X_train, y_train)

y_pred = xgbr.predict(X_test)

print(metrics.mean_squared_log_error(y_test, y_pred))

kaggle_pred = new_rfr.predict(test_df)
plt.scatter(X_train['GrLivArea'], y_train, c='blue', alpha=0.5)
plt.scatter(X_test['GrLivArea'], y_pred, c='green')
plt.scatter(test_df['GrLivArea'], kaggle_pred, c='red')

xgbr_output = np.vstack((test_ids, kaggle_pred)).T
submission = pd.DataFrame(xgbr_output, columns=['Id', 'SalePrice'])
submission.Id = submission.Id.astype(np.int)
submission.to_csv('../data/xgbr_output_submission.csv', index=False)
