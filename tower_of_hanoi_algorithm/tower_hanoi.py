# Recursive Python function to solve tower of hanoi 
  
def TowerOfHanoi(n, from_rod, to_rod, aux_rod): 
    global count
    count= 0
    if n == 0: 
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod) 
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
    count += 1
  
# Driver code 
N = 3
# A, C, B are the name of rods 
TowerOfHanoi(N, 'A', 'C', 'B') 
print("Stack Total Movement:  " , count)
  
# Contributed By Harshit Agrawal 
