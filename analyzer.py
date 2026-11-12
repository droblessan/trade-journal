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