n,m=map(int,input().split())

vis=[]
arr=[]

for _ in range(n):
    arr.append([])
    vis.append([])

for _ in range(n):
    # for i in range(m):
    u=input()
    arr[_].append(u.split())

# print('ans')
# print(arr[1][0][1])

# for _ in range(len(arr)):
#     print(arr[_])

# 5 8
# # # # # # # #
# . . # . . . #
# # # # . # . #
# . . # . . . #
# # # # # # # #

for _ in range(n):
    for i in range(m):
        if(arr[_][0][i]=='#'):
            vis[_].append(1)
        else:
            vis[_].append(0)

for _ in range(len(vis)):
    print(vis[_])

# print('ans')

# print(vis[1][0])
# print(vis)

ans=0

moves=[[-1,0],[1,0],[0,-1],[0,1]]

def valid(x,y):
    if(x<0 or x>=n or y<0 or y>=m):
        return False
    if(vis[x][y]==1):
        return False
    return True

def dfs(i,j):
    vis[i][j]=1
    for _ in range(len(moves)):
        if(valid(i+moves[_][0],j+moves[_][1])):
            dfs(i+moves[_][0],j+moves[_][1])

def cnctd():
    for _ in range(n):
        for i in range(m):
            if(vis[_][i]==0):
                dfs(_,i)
                ans+=1


print(ans)