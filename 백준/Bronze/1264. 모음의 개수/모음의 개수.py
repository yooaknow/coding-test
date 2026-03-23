while True:
    s = input()
    
    if s == "#":
        break
    
    count = 0
    for c in s:
        if c.lower() in "aeiou":
            count += 1
    
    print(count)