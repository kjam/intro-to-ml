isnumeric = train_df.dtypes.map(
        lambda x: np.issubdtype(x, int) or np.issubdtype(x, float))
numeric_cols = isnumeric[isnumeric == True].index.values
num_train_df = train_df[numeric_cols].copy()
