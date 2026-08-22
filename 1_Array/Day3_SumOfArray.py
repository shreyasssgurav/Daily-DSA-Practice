n = int(input("Enter the size of array:"))
arr = []

print("Enter the elements you want to insert:")
for i in range(n):
    arr.append(int(input()))
    
sum = 0

for i in range(0,n):
    sum = arr[i] + sum

print(f"The sum of array is {sum}")   