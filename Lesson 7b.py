trades = [
    {"result" : 2, "rules" : True},
    {"result" : -1, "rules" : False},
    {"result" : 3, "rules" : True},
    {"result" : -1.5, "rules" : True},
]
for trade in trades:
    print(trade["result"])

wins = 0
rules_broken = 0

for trade in trades:
    if trade["result"] > 0:
        wins += 1
    if not trade["rules"]:
        rules_broken += 1
print(f"Wins: {wins}")
print(f"Rules broken: {rules_broken}")