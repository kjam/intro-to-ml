print(count_nb.get_params())
grid_test = {
        'alpha': np.arange(0, 1.05, 0.05),
        'fit_prior': [True, False],
}
grid_search = GridSearchCV(estimator=count_nb, param_grid=grid_test)
grid_search.fit(count_train, y_train)
scores = grid_search.grid_scores_

top_score = sorted(scores, key=lambda x: x.mean_validation_score, reverse=True)[0]
print(top_score.parameters)

count_nb_final = MultinomialNB(alpha=0.05)
count_nb_final.fit(count_train, y_train)

pred = count_nb_final.predict(count_test)
score = metrics.accuracy_score(y_test, pred)
print("accuracy:   %0.3f" % score)
cm = metrics.confusion_matrix(y_test, pred, labels=[trump.name, trudeau.name])
plot_confusion_matrix(cm, classes=[trump.name, trudeau.name])
