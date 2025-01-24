items = ["apple", "banana", "orange", "apple", "mango", "orange"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ",item)
    unique_item.add(item)