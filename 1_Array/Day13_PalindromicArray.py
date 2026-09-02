n = int(input("Enter the size of array."))
arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

palindrom = 0
count = 0 

for i in range(n):
    element = arr[i]
    while(element > 0):
        a = element % 10
        palindrom = palindrom * 10 + a
        element = element // 10

    if(arr[i] == palindrom):
        count += 1

    palindrom = 0 

if(count == len(arr)):
    print(True)
else:
    print(False)    

   

