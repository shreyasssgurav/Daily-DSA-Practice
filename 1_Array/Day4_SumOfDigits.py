n = int(input("Enter the size of array:"))
arr = []

print("Enter the elements of array:")
for i in range(0,n):
    arr.append(int(input()))
    
print("The sum is:")    
sum = 0

for i in range(0,n):        
    while(arr[i] != 0):
        sum += arr[i] % 10
        arr[i] = arr[i] // 10
        
print(sum)    