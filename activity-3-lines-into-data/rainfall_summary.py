"""
Rainfall Summary

Reads a month's rainfall from five weather stations and prints a
summary. Reading only: nothing is written back out.

Each line of rainfall.txt is a station name and a number of
millimetres, separated by a comma.
"""

WET_THRESHOLD = 90

with open("rainfall.txt", "r") as f:
    lines = f.readlines()

total = 0
count = 0
driest = 0
wettest = 0
driest_station = " "
wettest_station = " "
wet_stations = []

for line in lines:
    station, millimetres_text = line.strip().split(",")
    millimetres = int(millimetres_text)

    if millimetres > wettest:
        wettest_station = station
        wettest = millimetres

    if driest == 0 or millimetres < driest:
        driest_station = station
        driest = millimetres

    total = total + millimetres
    count = count + 1

    if millimetres >= WET_THRESHOLD:
        wet_stations.append(station)

print(f"{count} stations reported")
print(f"Total rainfall: {total} mm")
print(f"Average: {total / count:.1f} mm")
print(f"At or above {WET_THRESHOLD} mm: {wet_stations}")
print(f"The driest station is {driest_station}")
print(f"The wettest station is {wettest_station}")
print(f"The number of stations below the threshold was {count - len(wet_stations)}")