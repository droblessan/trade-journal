from AnalyzerV2 import win_rate, average_r, average_r_by_rules, equity_curve, losing_streak

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

list4 = [
    {"result" : -1.0, "rules" : True},
    {"result" : -1.0, "rules" : False},
    {"result" : 2.0, "rules" : True},
    {"result" : -1.0, "rules" : True},
]

list5 = [
    {"result" : 2.0, "rules" : True},
    {"result" : 1.0, "rules" : False},
    {"result" : 3.0, "rules" : True},
]

list6 = [
   {"result" : -1.0, "rules" : True},
   {"result" : 0, "rules" : False},
   {"result" : -1.0, "rules" : True},
]

assert average_r_by_rules(list3, False) == 0, "broken average failed for list3"
assert win_rate(list3) == 50, "win rate failed for list3"
assert win_rate([{"result" : 0, "rules" : True}]) == 0, "break even only list failed"
assert equity_curve([]) == [], "equity curve failed for empty list"
assert equity_curve(two) == [2.0, 1.0], "equity curve failed for two"
assert equity_curve(list3) == [2.0, 1.0, 1.0], "equity curve failed for list3"
assert losing_streak([]) == 0, "losing streak failed for empty list"
assert losing_streak(list4) == 2, "losing streak failed for list4"
assert losing_streak(list5) == 0, "losing streak failed for list5"
assert losing_streak(two) == 1, "losing streak failed for two"
assert losing_streak([{"result" : 0, "rules" : True}]) == 0, "losing streak failed for break even only list"
assert losing_streak(list6) == 2, "Break even should not break losing streak"