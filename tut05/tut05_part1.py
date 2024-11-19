n = int(input("Enter number of elements : "))
nums = []
for i in range(n):
    num = int(input(f"Enter {i+1} element: "))
    nums.append(num)

result = set()

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if nums[i] + nums[j] + nums[k] == 0:
                triplet = sorted([nums[i] , nums[j] , nums[k]])
                result.add(tuple(triplet))
print(result)