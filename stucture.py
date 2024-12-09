# # list(array)(editable), set, tuple(un-editable), dictionaries

# # list

# # subjects = ["maths","science","english"]

# # print(subjects[0])

# # for x in subjects:
# #     print(x)

# # subjects = [56,75,88]

# # for x in subjects:
# #     print( f"{(x / 100 )* 100}%" )

# subjects = ["maths","science","english"]

# # print(subjects[0])

# # # length | element count

# # print(len(subjects)) 

# # subjects[0] = "history"

# # print(subjects[0])

# subjects[1:] = ["s1","s2"]

# print(subjects[1:])

# print(subjects)

# subjects.append("geo")

# subjects.insert(0,"new new element")

# subjects.insert(3,"element 3")

# print(subjects)


# newSubject = ["new list s1","new list s2","new list s3"]

# subjects.extend(newSubject)

# # subjects.pop()

# del subjects[0]

# subjects.clear()

# print(subjects)

# numbers = [5,2,1,4,3]

# print(numbers)

# numbers.sort()

# print(numbers)

numbers = [5,2,1,4,3]

even = []

odd = []

for x in numbers:
    if x % 2 == 0 :
        even.append(x)
    else:
        odd.append(x)
        
print(even)
print(odd)


nums = (2,1,3,4)

nums[0] = 123

print(nums)