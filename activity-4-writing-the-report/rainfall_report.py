"""
Rainfall Report

The same data as activity 3, but this time the summary goes into a
file rather than onto the screen. A working program.

Reads rainfall.txt, writes report.txt.
"""

WET_THRESHOLD = 100

with open("rainfall.txt", "r") as f:
    lines = f.readlines()

total = 0
count = 0

with open("report.txt", "w") as report:
    for line in lines:
        station, millimetres_text = line.strip().split(",")
        millimetres = int(millimetres_text)

        total = total + millimetres
        count = count + 1

        if millimetres >= WET_THRESHOLD:
            status = "Wet"
            report.write(f"{station}: {millimetres} mm ({status})\n")
        else:
            status = "Dry"
            print(f"{station}: {millimetres} mm ({status})\n")

        

    report.write(f"Number of stations: {count}\n")
    report.write(f"Total rainfall: {total} mm\n")
    report.write(f"Average: {total / count:.1f} mm\n")

print(f"Report written. {count} stations.")
