names = ["lenin", "arun", "kumar", "lenin","arun", "suresh", "kumar", "lenin", "arun", "kumar"]
for name in set(names):
    if names.count(name)> 1:
        print(name)