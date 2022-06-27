# def print_word(str:str):
#     """ This function get strings of list from user 
#         and returns strings without repetitions, each once
        
#         Args:
#             str (_list)"""

#     world = []

#     [world.append(x) for x in str if x not in world] 
#     return world
# str = []

# while (inp := input("Enter word:> ")):
#     str.append(inp)
# print(print_word(str))


# def print_divisors(numb:int):
#     """This function get number as an arg 
#          Returns list divsors of number
        
#         Args:
#             numb (_int)"""

#     result = []

#     for i in range(1, numb//2 + 1):
#         if numb % i == 0:
#             result.append(i)
#     result.append(numb)
#     return result
   

# numb = int(input("Enter number:> "))
# print(print_divisors(numb))



# def check_perfect_number(n:int):
    # """This function get number as an arg, check is the number perfect number or not 
    #         (perfect number is a positive integer that is equal to the sum of its positive divisors, 
    #          excluding the number itself.)
    #     if the number is perfect Returns  TRUE else FALSE
        
    #      Args:
    #          n (_int)"""
    
#     divisors = []

#     for i in range(1, n//2 + 1):
#         if n % i == 0:
#             divisors.append(i)
    
#     if sum(divisors) == n:
#         return True
#     return False

# n = int(input("Enter number:> "))
# print(check_perfect_number(n))



# def my_zip(data1,data2):
    # """This function get 2 list  as an arg,  
    #    Returns iterator of lists
        
    #      Args:
    #          data1 (_list)
    #          data2 (_list)"""

#     result = []

#     for i in range(len(data1)):
#         result.append([data1[i], data2[i]])   
    
#     return result
    
# data1 = [1,2,3]
# data2 = ["a","b","c"]
# print(my_zip(data1,data2))



# def check_palindromes(str):
#     """This function get sentence as an arg,  
#         if the sentence is palimdrome Returns message
            
#             Args:
#                 str (_string)"""

#     marks = '''!;:'"\,./?'''

#     for i in marks:
#         if i in str:
#             str = str.replace(i,"")
    
#     if str.lower().split()[0] == str.lower().split()[-1]:
#         return "Sentence is a palindrome"

# str = input("Enter sentence:>  ")
# print(check_palindromes(str))




# def get_numbers(numb:int):

#     med = 0
#     list_small = []
#     list_equal = []
#     list_biger = []
#     for i in numb:
#         med+= i
#         if med/len(numb) > i:
#             list_small.append(i)
#         elif med/len(numb) == i:
#             list_equal.append(i)
#         else:
#             list_biger.append(i)

#     return med/len(numb), list_small,list_equal, list_biger   
    

# print(get_numbers([4,5,2,5,10]))


# import random 

# def prize():
#     """This function returns random 6 number for ticket and showen in ascending order"""

#     ticket = []

#     for i in range(1,7):
#         n = random.randint(1,49)
#         if n not in ticket:
#             ticket.append(n) 
#     ticket.sort()
#     return ticket
# print(prize())




# def is_sorting(n:int):
#     """This function get numbers,  
#          if the list of nubmers is in ascending order Return True Else False
            
#              Args:
#                  n (_int)"""

#     numb = [i for i in str(n)]
#     if numb is sorted:
#         return True
#     i = 1
#     while i < len(numb):
#         if(numb[i-1] <= numb[i]):
#             return True
#         else:
#             return False
#     i += 1

# n = int(input("Enter numbers:> "))
# print(is_sorting(n))



