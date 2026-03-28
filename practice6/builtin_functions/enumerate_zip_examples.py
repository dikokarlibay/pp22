
fruits = ["apple", "banana", "cherry"]
prices = [1.2, 0.5, 3.0]

for i, fruit in enumerate(fruits):
    print(i, fruit)

for fruit, price in zip(fruits, prices):
    print(fruit, price)

fruit_prices = dict(zip(fruits, prices))
print(fruit_prices)

nums = [3, 1, 4, 1, 5, 9]
print(len(nums))
print(sum(nums))
print(min(nums))
print(max(nums))
print(sorted(nums))

print(int("42"))
print(float("3.14"))
print(str(100))
print(bool(0))
print(list((1, 2, 3)))
print(set([1, 2, 2, 3]))
