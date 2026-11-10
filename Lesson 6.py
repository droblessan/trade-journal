runs = [3, 5, 2, 8, 6]
print(runs[0])
print(runs[4])
runs.append(4.5)
print(runs[5])
print((f"Total: {sum(runs)}"), (f"Min: {min(runs)}"), (f"Max: {max(runs)}"))
for miles in runs:
    if miles > 4:
        print(miles)

win = 0
trades = [1.5, -1, 2, -1, -1, 3]
for result in trades:
    if result > 0:
        win += 1
print(f"Total: {win}")