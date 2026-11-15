T = int(input ())

for i in range(T):
    
    def inorder(i):
        global num 
        
        if i > N:
            return
        
        inorder(i*2)
        tree[i] = num
        num += 1 
        inorder(i*2+1)
    
    N = int(input())
    tree = [0]*(N+1)
    num = 1
    
    inorder(1)
    
    n1 = tree[1]
    n2 = tree[N//2]
    
    print(f"#{i+1} {n1} {n2}")