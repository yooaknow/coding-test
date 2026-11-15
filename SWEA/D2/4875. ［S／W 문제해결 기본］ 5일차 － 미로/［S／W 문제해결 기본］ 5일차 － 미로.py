T = int(input())

for i in range(T):
  num = int(input())
  a = []
  answer = 0
  
  for j in range(num):
    a.append(list(map(int, input().strip())))
    
  for h in range(len(a)):
        for j in range(len(a[h])):
            if a[h][j] == 2:
              start = [h, j]
            if a[h][j] == 3:
              end = [h,j]
            
  x,y = start
  z,e = end
  visited = [[False]*num for _ in range(num)]
  visited[x][y] = True
  stack = [start]
  
  while stack:
    x,y = stack.pop()
    
    if x == z and y == e:
      answer = 1
      break
  
    if x+1<len(a) and a[x+1][y]!=1 and not visited[x+1][y]:
      visited[x+1][y] = True
      stack.append([x+1, y])
      
    if x-1>=0 and a[x-1][y]!=1 and not visited[x-1][y]:
      visited[x-1][y] = True
      stack.append([x-1, y])
      
    if y-1>=0 and a[x][y-1]!=1 and not visited[x][y-1]:
      visited[x][y-1] = True
      stack.append([x, y-1])
      
    if y+1<len(a[x]) and a[x][y+1]!=1 and not visited[x][y+1]:
      visited[x][y+1] = True
      stack.append([x, y+1])
      
  print(f"#{i+1} {answer}")