print("======CONSUMER TRANSACTION TRACKER======")

transactions = []

for i in range(5):
    value = float(input("Enter transaction amount: "))
    transactions.append(value)

largest = max(transactions)
smallest = min(transactions)
average = sum(transactions) / len(transactions)

print("\n======TRANSACTION SUMMERY======")

print("Largest transaction amount:", largest)
print("Smallest transaction amount:", smallest)
print("Average spend:", average)