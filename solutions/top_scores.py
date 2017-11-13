top_scores = sorted(scores, key=lambda x: x.mean_validation_score, reverse=True)[:5]
print(top_scores)
