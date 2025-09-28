# Write a function that takes a list and returns the maximum number.

l1 = [20, 40, 38, 29]
print(len(l1))


def maximum(nums):
    max_num = 0
    n = len(l1)
    for i in range(n):
        # print(nums[i])

        if nums[i] > max_num:
            max_num = nums[i]
    return max_num

        
        
# maximum(l1)

result = maximum(l1)

print(result)

    
 


    
# Write a function that takes a dictionary {name and marks} and returns the topper.

# name_marks_dct = {
#         "Aakash":  49, 
#        "Rupali": 68,
#        "John": 96,
#        "Poulomi": 80
#     }

# def topper(name_marks_dct):
#     topper = " "
#     max_marks = 0
#     for name, marks in name_marks_dct.items():
#         if marks > max_marks:
#             max_marks = marks
#             topper = name
#     return topper

# print(topper(name_marks_dct))



