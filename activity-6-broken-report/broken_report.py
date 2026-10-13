"""
Rainfall Report

Three things below are wrong. Nothing crashes.

Reads rainfall.txt, writes report.txt. It is meant to produce one
line per station, followed by the average, and to produce the same
report every time it is run.
"""

WET_THRESHOLD = 100
WATCH_LIST = ["Manchester", "Cardiff"]

with open("rainfall.txt", "r") as f:
    contents = f.read()

record_count = len(contents.strip().split("\n"))

total = 0

with open("report.txt", "w") as report:
    for line in contents.splitlines():
        station, millimetres_text = line.split(",")
        millimetres = int(millimetres_text)

        total = total + millimetres

        if station.strip() in WATCH_LIST:
            status = "Watch"
        elif millimetres >= WET_THRESHOLD:
            status = "Wet"
        else:
            status = "Dry"

        report.write(f"{station.strip()}: {millimetres} mm ({status})\n")

    report.write(f"Average: {total / record_count:.1f} mm\n")

print(f"Report written. {record_count} stations.")
