n = int(input("Enter the size of array:"))
arr = []

print("Enter the elements you want to insert:")
for i in range(n):
    arr.append(int(input()))

revArr = []

for i in range(n-1,-1,-1):
    revArr.append(arr[i])

print(f"Original array : {arr}")
print(f"Reverse Array : {revArr}")    