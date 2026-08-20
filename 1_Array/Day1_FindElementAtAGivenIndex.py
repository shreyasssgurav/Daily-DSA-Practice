n = int(input("Enter the size of array."))
arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

index = int(input(f"Enter the index(0-{n}):"))
res = arr[index]

print(f"The element found at given index is {res}")
print(arr)