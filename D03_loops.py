daily_sales = [1200, 950, 0, 1800, 2200, 0, 1500]

total_sales = 0
days_with_no_sales = 0

for day_index in range(len(daily_sales)):
    sale = daily_sales[day_index]

    if sale == 0:
        days_with_no_sales += 1
        continue
    total_sales  += sale

average_sales = total_sales / (len(daily_sales) - days_with_no_sales)

print(f"Total sales: {total_sales}")
print(f"Days with no sales: {days_with_no_sales}")
print(f"Average sales (active days only): {average_sales:.2f}")

# while loop example
stock = 50
orders_filled = 0

while stock > 0:
    stock -= 7
    orders_filled += 1

print(f"Orders filled before stock ran out: {orders_filled}")
print(f"Remaining stock (could go negative): {stock}")

