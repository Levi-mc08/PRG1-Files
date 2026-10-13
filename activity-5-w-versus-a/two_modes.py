"""
Two modes

The shortest program in the module, and the one whose behaviour you
are most likely to get wrong in an assignment.

Run it. Then run it again. Then look at both files.
"""
import os

with open("overwrite.txt", "w") as f:
    f.write("A line\n")

with open("append.txt", "a") as f:
    f.write("A line\n")

with open("overwrite.txt", "r") as f:
    print(f"overwrite.txt now has {len(f.readlines())} line(s)")

with open("append.txt", "r") as f:
    print(f"append.txt now has {len(f.readlines())} line(s)")
