total_r = 0
win = 0
trades = [1.5, -1, 2, -1, -1, 3]
for result in trades:
    total_r += result
    if result > 0:
        win += 1
print(f"Wins: {win}")
print(f"Win Percentage: {win / len(trades) * 100}%")
print(f"Average R: {round(total_r / len(trades), 2)}")
