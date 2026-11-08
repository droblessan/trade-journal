paid_hours = [8.5, 6, 7.5, 9.5, 5, 8.5]
total = 0
overtime = 0
for hours in paid_hours:
    total = total + hours
    if hours > 8:
        overtime = overtime + (hours - 8)
        print(f"{hours - 8} h: Overtime")
print(f"Total Overtime: {overtime} h")
print(f"Total Hours: {total}")
if total >= 50:
    print("Clears floor")
else :
    print("Needs hours")

average_hours = round(total / len(paid_hours), 2)
print(f"Average hours {average_hours}")