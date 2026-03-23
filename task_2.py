curriculum = []

for week in range(1, 17):
    if week % 4 == 0:
        curriculum.append("Контроль")
    else:
        curriculum.append(4)

print("Учебный план на семестр:")
print(curriculum)

# Комментарий:
# Идем по неделям с 1 до 16.
# Каждая 4-я неделя — "Контроль", остальные — 4 часа.
