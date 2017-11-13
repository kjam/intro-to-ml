print(num_train_df[num_train_df.MasVnrArea.isnull()])
num_train_df.MasVnrArea = num_train_df.MasVnrArea.fillna(0)
