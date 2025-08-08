numbers = list(map(int, input("Input: ").split()))
result = {}
for i in range(1, 10):
    result[i] = 0
for i in range(1, 10):
    for num in numbers:
        if num % i == 0:
            result[i] += 1

print("Output:", result)
