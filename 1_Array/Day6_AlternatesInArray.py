n = int(input("Enter the size of array:"))
arr = []

print("Enter the elements you want to insert:")
for i in range(n):
    arr.append(int(input()))

arr2 = []
for i in range(0,n,+2):
    arr2.append(arr[i])

print(arr2)    