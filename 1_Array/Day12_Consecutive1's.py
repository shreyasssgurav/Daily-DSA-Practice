n = int(input("Enter the size of array."))
arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))


consecutive = 0
consecutive1 = 0

for i in range(n):
    if(arr[i] == 1):
        consecutive += 1
         
        if(consecutive > consecutive1):
            consecutive1 = consecutive
    else:
        consecutive = 0    


print(f"Maximum Consecutive 1's count is {consecutive1}")  