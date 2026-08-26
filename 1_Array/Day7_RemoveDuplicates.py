n = int(input("Enter the size of array:"))
arr = []
k = 0

print("Enter the elements you want to insert:")
for i in range(n):
    arr.append(int(input()))

newArr =  []  

for i in range(n):
    if(arr[i] not in newArr):
         newArr.append(arr[i])

print("New Array:",newArr)
k = len(newArr)
print(f"The length of array after removing duplicate elements is {k}")

