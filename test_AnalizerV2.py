from AnalyzerV2 import win_rate, average_r, average_r_by_rules

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

assert average_r_by_rules(two, True) == 2.0, "followed average failed"
assert average_r_by_rules(two, False) == -1.0, "broken average failed"

list3 = [
    {"result" : 2.0, "rules" : True},
    {"result" : -1.0, "rules" : True},
    {"result" : 0, "rules" : True},
]

assert average_r_by_rules(list3, False) == 0, "broken average failed for list3"
assert win_rate(list3) == 50, "win rate failed for list3"
assert win_rate([{"result" : 0, "rules" : True}]) == 0, "break even only list failed"