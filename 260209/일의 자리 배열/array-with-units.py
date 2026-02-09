N, M = map(int, input().split())

arr = [N, M]

for i in range(8):
    num = (arr[i] + arr[i+1]) % 10  
    arr.append(num)

print(*arr)