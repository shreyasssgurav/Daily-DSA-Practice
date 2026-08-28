n = int(input("Enter the size of array:"))
arr = []
k = 0

print("Enter the elements you want to insert:")
for i in range(n):
    arr.append(int(input()))

largest = float('-inf')
secondLargest = float('-inf')

for i in range(0,n):
    if(arr[i] > largest):
        largest = arr[i]

for i in range(n):
    if(arr[i] > secondLargest and arr[i] is not largest):
        secondLargest = arr[i]        


print(f"\nThe second largest array element from the array is {secondLargest}")
