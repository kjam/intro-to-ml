rfr_output = np.vstack((test_ids, kaggle_pred)).T
submission = pd.DataFrame(rfr_output, columns=['Id', 'SalePrice'])
submission.Id = submission.Id.astype(np.int)
submission.to_csv('../data/rfr_output_submission.csv', index=False)
