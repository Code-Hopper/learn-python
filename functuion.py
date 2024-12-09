# # syntax for a function
# def doSomething():
#     print("doing something !")
    
# def add(x,y):{
#   print(x+y)  
# }

# add(5,45)

# nums = [1,2,3,4,5]

# # for element in nums: 
# #     print(element)

# def makeSquare(list):
#     for item in list:
#         print(item*item)
        

# print(makeSquare(nums))

# def hello(name = "default"):
#     print(f"hello ! {name}")
    
# hello("amey")

a = 1
b = 2
c = 3

def findMax(*numbers):
    # return the largest number in the tupple
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
    
print(findMax(10,255,30,400,13890712390,-90,89071298,12351678))