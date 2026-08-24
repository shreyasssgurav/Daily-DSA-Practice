n = int(input("Enter the size of array:"))
arr = []

print("Enter the elements you want to insert:")
for i in range(n):
    arr.append(int(input()))

sort = True

for i in range(n-1,0,-1):
    if(arr[i] < arr[i-1]):
        sort = False

if sort:        
    print("Array is sorted.")
else:
    print("Array is not sorted.")    
