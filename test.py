import random # random number generator
import sys # system module
import os

# # lambda
# # Syntax: lambda arguments: expression
#
# greeter = lambda x: print('Hello %s!' %x)
# print(greeter('Albert'))
#
# all_names = ['surname', 'rename', 'nickname', 'acclaims', 'defame']
# filtered_names = list(filter(lambda x: 'name' in x, all_names))
# print(filtered_names)

# list_a = [1,2,3,4,5]
# filter_obj = filter(lambda x: x%2 == 0, list_a) # returns filter object,
# # cant use index or len()
# print(list(filter_obj))

print(list(map(lambda x: x*2, [2,4,6,8])))

# # sys examples
# sys.stderr.write('this is stderr test\n') # in red
# sys.stderr.flush()
# sys.stdout.write('this is stdout test\n') # in blue
#
# # os examples
# # print current directory
# print(os.getcwd())
#
#
# '''
# Multiple line
# Comments
# '''
#
# # Strings - mutable type
# grocery_list = ['juice','tomatoes','potatoes','bannas']
# print('first item', grocery_list[0])
# # change the first item
# grocery_list[0] = 'Green Juice'
# print('first item', grocery_list[0])
#
# print(grocery_list[1:3])
# other_events = ['wash car','pick up kids','cash check']
# # combine two lists: list within a list
# to_do_list = [other_events, grocery_list]
# print(to_do_list) # [['wash car', 'pick up kids', 'cash check'], ['Green Juice', 'tomatoes', 'potatoes', 'bannas']]
#
# # list can have items of different types
# to_do_list.append('onions') #[['wash car', 'pick up kids', 'cash check'], ['Green Juice', 'tomatoes', 'potatoes', 'bannas'], 'onions']
# print(to_do_list)
#
# grocery_list.insert(1,"pickle") # insert "pickle" at position one
# print(grocery_list)
#
# grocery_list.remove("pickle")
# grocery_list.sort()
# grocery_list.reverse()
#
#
# print(grocery_list)
# del grocery_list[2]
# print(to_do_list) # deletion in grocery_list also makes changes in the
# # grocery_list in to do list
#
# print(min(other_events)) # print min one alphabetically

# ---------- BELOW is about tuple

# pi_tuple = (3,1,4)
# new_tuple = list(pi_tuple)
# new_list = tuple(new_tuple) # change tuple to list and convert back to tuple
#
# # ---------- BELOW is condition
#
# age = 21
#
# if age > 16:
#     print(" you are old enough to drive")
# else:
#     print("you are not old enough to drive")
#
# if ((age >= 1) and (age <= 18)):
#     print("you get a birthday")
# elif (age ==21) or(age >= 65):
#     print(" you get a")
# else:
#     print("nothing")
#
#
# for x in range(0,10): # 0 up to 10, not include 10
#     print(x, " ", end=" ")
#
#
# def addNumber(fNum, lNum):
#     sumNum = fNum + lNum
#     return sumNum
#
# print(addNumber(1,4))

# class Animal:
#     __name = None  # with "__" means these are private, to change value,
#     # a class function is needed
#     __height = 0
#     __sound = 0
#
#     # constructor: set up initialize an object
#     def __init__(self, name, height, sound):
#         self.__name = name
#         self.__height = height
#         self.__sound = sound
#
#     def set_name(self, name): # self: allow the object referes to itself inside
# # this class
#         self.__name = name
#
#     def get_name(self): # this method - encapsulation
#         return self.__name
#
#     def get_type(self):
#         print("Animal")
#
#     def toString(self):
#         return "{} is {} cm tall and say {}".format(self.__name,
#                                                     self.__height, self.__sound)
#
# cat = Animal("kira",10, "Meow")
# print(cat.toString())
#
# # inheritance
# class Dog(Animal):
#     __owner = ""
#
#     def ___init__(self,name,height, sound, owner):
#         self.__owner = owner
#         super(Dog,self).__init__(name,height,sound)
#
#     def set_owner(self, owner):
#         self.__owner = owner