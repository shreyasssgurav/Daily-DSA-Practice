#MY APPROACH
n = int(input("Enter the size of array."))
arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    if(arr[i] == 1):
        arr.append(1)
        arr.remove(arr[i])

print(arr)
        
#ACTUAL APPROACH
# n = int(input("Enter the size of array: "))

# arr = []

# print("Enter the elements:")

# for i in range(n):
#     arr.append(int(input()))

# zero = arr.count(0)
# one = arr.count(1)

# arr = [0] * zero + [1] * one

# print(arr)