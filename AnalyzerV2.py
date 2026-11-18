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
    decided = 0
    for trade in trades:
        if trade["result"] > 0:
            wins += 1
        if trade["result"] != 0:
            decided += 1
    if decided == 0:
        return 0
    return wins / decided * 100

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

def equity_curve(trades):
    equity = 0
    curve = []
    for trade in trades:
        equity += trade["result"]
        curve.append(equity)
    return curve

#brakeven trades neither extend nor break a losing streak.
def losing_streak(trades):
    streak = 0
    max_streak = 0
    for trade in trades:
        if trade["result"] < 0:
            streak += 1
            if streak > max_streak:
                max_streak = streak
        elif trade["result"] > 0:
            streak = 0
    return max_streak

def main():
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
    print(f"Equity curve: {equity_curve(trades)}")
    print(f"Losing streak: {losing_streak(trades)}")
if __name__ == "__main__":
    main()

