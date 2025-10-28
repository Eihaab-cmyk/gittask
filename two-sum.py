nums = [2,7,11,15]
target = 9
output = []

seen = {}
for i, num in enumerate(nums):
    diff = target - num
    if diff in seen:
         [seen[diff], i]
    seen[num] = i
    print(seen)

print(seen)