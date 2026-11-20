
from AnalyzerV2 import  load_trades, win_rate, average_r, average_r_by_rules, equity_curve, losing_streak, main, average_r_by_instrument

mixed = [
    {"result" : 2.0, "rules" : True, "instrument" : "MCL"},
    {"result" : 4.0, "rules" : True, "instrument" : "MCL"},
    {"result" : -1.0, "rules" : False, "instrument" : "MES"},
    {"result" : 0, "rules" : True, "instrument" : "M6E"},
]

assert average_r_by_instrument(mixed, "MCL") == 3.0, "MCL average failed"
assert average_r_by_instrument(mixed, "MES") == -1.0, "MES average failed"
assert average_r_by_instrument(mixed, "M6E") == 0, "M6E average failed"
assert average_r_by_instrument(mixed, "XYZ") == 0, "Unknown average failed"