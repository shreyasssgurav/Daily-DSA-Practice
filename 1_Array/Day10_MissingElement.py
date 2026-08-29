n = int(input("Enter the size of array:"))
arr = []

r = int(input("Enter the range:"))

print("Enter the elements you want to insert:")
for i in range(n):
    arr.append(int(input()))


for i in range(0,r+1):
    if(i not in arr):
        print(i)    