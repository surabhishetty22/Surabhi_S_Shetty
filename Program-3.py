a = int(input("Input: "))
if a % 2 == 0:
    count = a - 1
else:
    count = a

series = []
for i in range(1, count + 1):
    series.append(2 * i - 1)
print("Output:", series)
