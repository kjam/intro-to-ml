set(df.columns) - set(df.dropna(thresh=df.shape[0] * .2, axis=1).columns)
