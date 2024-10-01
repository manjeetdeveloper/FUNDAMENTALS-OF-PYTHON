scores = [85, 92, 78, 92, 90, 85, 78, 88]
must_scores = list(set(scores))
print(must_scores)


max_score = max(must_scores)
min_score = min(must_scores)
print("Maximum Score:", max_score)
print("Minimum Score:", min_score)


must_scores.remove(min_score)
print("Changed Scores:", max_score)



