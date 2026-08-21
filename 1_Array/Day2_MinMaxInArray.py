n = int(input("Enter the size of array:"))
arr = []

print("Enter the elements you want to insert:")
for i in range(n):
    arr.append(int(input()))
    
min = float('inf')

for i in range(n):
    if arr[i] < min:
        min = arr[i]

max = float('-inf')
for i in range(n):
    if arr[i] > max:
        max = arr[i]

print(f"Minimun element from the array is {min}")    
print(f"Maximun element from the array is {max}")