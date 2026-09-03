n = int(input("Enter the size of array:"))
arr  = []

print("Enter the Elements you want to insert:")
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    if(arr[i] == 0):
        arr.append(0)
        arr.remove(arr[i])

print(arr)