print(final_test_df[final_test_df.isnull().any(axis=1)])
final_test_df.columns[final_test_df.isnull().any()].tolist()
final_test_df = final_test_df.fillna(0)
