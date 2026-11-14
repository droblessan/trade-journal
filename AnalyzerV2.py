import csv

def load_trades(filename):
    trades = []
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            trades.append({
            "date" : row["date"],
            "result" : float(row["result"]),
            "rules" : row["rules"] == "True",
            })
    return trades

def win_rate(trades):
    wins = 0
    for trade in trades:
        if trade["result"] > 0:
            wins += 1
    if len(trades) == 0:
        return 0
    return wins / len(trades) * 100

def average_r(trades):
    total = 0
    for trade in trades:
        total = total + trade["result"]
    if len(trades) == 0:
        return 0
    return total / len(trades)

def average_r_by_rules(trades, followed):
    results = []
    for trade in trades:
        if trade["rules"] == followed:
            results.append(trade["result"])
    if len(results) == 0:
        return 0
    return sum(results) / len(results)

try:
    trades = load_trades("trades.csv")
except FileNotFoundError:
    print("Could not find that file. Check the name and folder")
    trades = []
except ValueError:
    print("A result in your file is not a number")
    trades = []

print(f"Loaded {len(trades)} trades")
print(f"Win rate: {round(win_rate(trades), 2)}%")
print(f"Average result: {round(average_r(trades), 2)}")
print(f"Rules followed average result: {round(average_r_by_rules(trades, True), 2)}")
print(f"Broken rules average result: {round(average_r_by_rules(trades, False), 2)}")


#test
two = [
    {"result" : 2.0, "rules" : True},
    {"result" : -1.0, "rules" : False},
]

wcases = [
    ([], 0),
    ([
        {"result" : 2.0},
        {"result" : -1.0},
        ],50),
    ([
       {"result" : 2.0},
       {"result" : 1.0},
    ], 100),

]
for trades, expected in wcases:
  assert win_rate(trades) == expected, f"win_rate failed for {trades}"
cases = [
    ([], 0),
    ([
         {"result" : 2},
         {"result" : -1},
    ], 0.5)
]
for trades, expected in cases:
    assert average_r(trades) == expected, f"average_r failed for {trades}"