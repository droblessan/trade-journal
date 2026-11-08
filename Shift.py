days = float(input("How many days are you working this week? "))
start = float(input("Shift start "))
end = float(input("Shift end "))
lunch = float(input("Lunch time "))

def paid_hours(start, end, lunch):
    return(end - start - lunch)

paid = paid_hours(start, end, lunch)

def weekly_total(paid, days):
    return(paid * days)

hours = weekly_total(paid, days)

def clears_floor(hours):
    if hours >= 50:
        return("Clears floor")
    else :
        return("Needs more hours")

floor = clears_floor(hours)
print(floor)
print(f"Weekly paid hours: {hours}")