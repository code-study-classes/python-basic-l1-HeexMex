prices = [1500, 6000, 4999, 12000, 800]
new_prices = [price * 0.8 if price > 5000 else price for price in prices]

print("Старые цены:", prices)
print("Новые цены:", new_prices)

# Комментарий:
# Через list comprehension:
# если цена > 5000, применяем скидку 20% (умножаем на 0.8),
# иначе оставляем цену без изменений.
