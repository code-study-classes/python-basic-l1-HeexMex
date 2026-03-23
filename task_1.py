import random


scores = [random.randint(1, 100) for _ in range(7)]
print("Исходные баллы:", scores)

min_score = min(scores)
max_score = max(scores)

filtered_scores = scores.copy()
filtered_scores.remove(min_score)
filtered_scores.remove(max_score)

average_rating = sum(filtered_scores) / len(filtered_scores)

print("Средний рейтинг:", average_rating)