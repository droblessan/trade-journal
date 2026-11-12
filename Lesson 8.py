trades = [
    {"date" : "2026-11-11" , "result" : -3 , "rules" : True},
    {"date" : "2026-11-11" , "result" : 2 , "rules" : True},
    {"date" : "2026-11-11" , "result" : 5 , "rules" : True},
    {"date" : "2026-11-11" , "result" : -1 , "rules" : False},
    {"date" : "2026-11-12" , "result" : 1 , "rules" : False},
    {"date" : "2026-11-12" , "result" : 3 , "rules" : True},
    {"date" : "2026-11-12" , "result" : -1.5 , "rules" : False},
    {"date" : "2026-11-12" , "result" : 3.5 , "rules" : True},
]

def win_rate(trades):
    wins = 0
    for trade in trades:
        if trade["result"]> 0:
            wins += 1
    return wins / len(trades) * 100
print(round(win_rate(trades), 2))

def average_r(trades):
    total = 0
    for trade in trades:
        total = total + trade["result"]
    return total / len(trades)
print(round(average_r(trades), 2))

def average_r_by_rules(trades, followed):
    results = []
    for trade in trades:
        if trade["rules"] == followed:
            results.append(trade["result"])
    if len(results) == 0:
        return 0
    return sum(results) / len(results)
print(average_r_by_rules(trades, True))
print(average_r_by_rules(trades, False))

import csv
trades = []
with open("trades.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        trades.append({
            "date" : row["date"],
            "result" : float(row["result"]),
            "rules" : row["rules"] == "True",
        })
print(trades)