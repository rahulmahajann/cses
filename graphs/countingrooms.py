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

print('ans')
print(arr[1][0][1])

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

# for _ in range(len(vis)):
#     print(vis[_])

# print(vis)

