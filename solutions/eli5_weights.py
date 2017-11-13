new_rfr = pickle.load(open('../data/models/new_rfr.sav', 'rb'))
weights_df = eli5.explain_weights_df(new_rfr)
weights_df['feature_name'] = weights_df.feature.map(lambda x: feature_names[x] if x in feature_names else x)
weights_df.sort_values('weight', ascending=False)
