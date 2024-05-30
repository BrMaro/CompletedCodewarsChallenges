def dead_ant_count (ants):
    stack=[]
    for char in ants:
        if char == "a" and len(stack)==0:
            stack.append("a")
        elif char == "n" and len(stack)==1:
            stack.append("n")
        elif char == "t" and len(stack)==2:
            stack.append("t")
            stack.clear()
        else:
            print("dead ant")


print(dead_ant_count("ant ant ant ant"))
print("\n")
print(dead_ant_count("ant anantt aantnt"))