"""
Reading a file

The same file, read three different ways. The output is not the same
each time, and the differences are the whole point of this activity.
"""

with open("rainfall.txt", "r") as f:
    whole_thing = f.read().strip()

print("--- 1: the whole file as one string ---")
print(whole_thing)

with open("rainfall.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

print("--- 2: a list of lines ---")
print(lines)
print(f"{len(lines)} lines")

with open("rainfall.txt", "r") as f:
    print("--- 3: one line at a time ---")
    for line in f:
        line = line.strip()
        print(f"[{line}]")

# print(lines[2])