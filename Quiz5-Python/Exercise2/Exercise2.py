import csv

import csv

stats = {}

try:
    with open('products.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            try:
                name, price, quantity = row
                price = float(price)
                quantity = int(quantity)
                if name not in stats:
                    stats[name] = {'price': price, 'quantity': 0, 'total': 0}
                stats[name]['total'] += price * quantity
                stats[name]['quantity'] += quantity
            except ValueError:
                print(f"Invalid input {row}")

except FileNotFoundError:
    print("File not found")

with open('backet.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',')
    for key, value in stats.items():
        csv_writer.writerow([key, value['price'], value['total'], value['quantity']])




