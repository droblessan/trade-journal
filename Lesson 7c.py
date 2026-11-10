trades = [
    {"result" : 3, "rules" : True},
    {"result" : 1, "rules" : False},
    {"result" : -0.5, "rules" : True},
    {"result" : -2, "rules" : False},
    {"result" : 3, "rules" : True},
]
trades.append({"result" : 2, "rules" : True})

followed = []
broken = []

for trade in trades:
    if trade["rules"]:
        followed.append (trade["result"])
    else:
        broken.append (trade["result"])

print(f"Rules followed: {round(sum(followed) / len(followed), 2)} Average R")
print(f"Rules broken: {round(sum(broken) / len(broken), 2)} Average R")