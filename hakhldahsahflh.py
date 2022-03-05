import collections
# nums = [3,3,3,4,4,4,4,2,2]
# [3,3,3,4,2]
# nums = [3,4,2]
# nums = [2,2,3,3,3,4]
nums = [8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4] #out60 exp61


points = 0 # total points added
nums.sort(reverse=True)
# higher number needs to be added first to earn high points
print(nums)

# run all the way till empty to get all points i can get
while nums != []: 
    # count all nums
    counter_dict = collections.Counter(nums)
    # order by the most common num
    most_common = counter_dict.most_common()
    # and get the most frequent num
    # because starting from the smallest can delete big points... 
    (num,cnt) = most_common[0]
    # num to be added and deleted
    to_add = nums.pop(nums.index(num))
    points += to_add

    # delete other numbers +-1
    for num in nums:
        # if (to_add == num + 1) or (to_add == num - 1):
        if (num == to_add + 1) or (num == to_add - 1):
            nums.pop(nums.index(num)) 
    # refresh counter
    counter_dict = collections.Counter(nums)
    # print(most_common,to_add,counter_dict,points)
    print(f"{nums}\nadd {to_add} points! total {points}")
print(points)