# Count the number of ways to reach the nth staire 

def find_way_to_reach(n):
    if n<=1:
        return n
    return find_way_to_reach(n-1)+find_way_to_reach(n-2)

n=2
print(find_way_to_reach(n+1))