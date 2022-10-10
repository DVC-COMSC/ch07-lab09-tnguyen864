# List for 5 names
names = []

# Get 5 names
print("Enter 5 names: ")
for i in range(5):
    name = input()
    names.append(name)

# Sort list
names.sort()

# Get shortest and longest string
shortest = min(names, key = len)
longest = max(names, key = len)

# Print shortest and longest string
print("Shortest:", shortest)
print("Longest:", longest)