n = int(input("Enter the size of array:"))
arr = []

print("Enter the elements you want to insert:")
for i in range(n):
    arr.append(int(input()))


#MY APPROACH
# for i in range(n):
#             if arr[i] == 1:
#                 arr.append(arr[i])
#                 arr.remove(arr[i])

# for i in range(n):
#             if arr[i] == 2:
#                 arr.append(arr[i])
#                 arr.remove(arr[i])

zero = 0
one = 0
two = 0

for i in range(n):
    if(arr[i] == 0):
        zero += 1
    if(arr[i] == 1):
            one += 1
    if(arr[i] == 2):
            two += 1

arr = [0] * zero + [1] * one + [2] * two

print(arr)                