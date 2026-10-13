"""
Optional stretch. What happens when the file is not there.

Run it as it is. Then create a file called notes.txt next to this
one, put a line in it, and run it again.
"""

FILENAME = "notes.txt"



print("--- without any protection ---")
try:
    with open(FILENAME, "r") as f:
        print(f.read())
except FileNotFoundError as problem:
    print(f"Caught it: {problem}")
    print(f"Could not find a file with name: {FILENAME}")

print("--- deciding what to do instead ---")
try:
    with open(FILENAME, "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    lines = []

print(f"{len(lines)} line(s) to work with")
