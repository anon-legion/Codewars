# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 21:09:03 2021

@author: =GV=
"""

def digital_root(n):
    while len(toStr := str(n)) > 1:
        n = 0
        for digit in toStr:
            n += int(digit)
    return int(toStr)


#def digital_root(n):
    """
        In order to get the correct answer, "n % 9 or n and 9" is used. The purpose of this is to return "9" in any case where the remainder is 0. Remember, in python "and" statements are evaluated first, so the order of operations is:
            
        n % 9 or (n and 9)
        
        "int and int" will return the second number if the first is anything other than 0. So for any integer, positive or negative, that is not 0, the above statment will be reduced to:
            
        n % 9 or 9
        
        "int or int" is the opposite of the above. If the first number is anything other than 0, it will return the first number, otherwise the second number is returned. So the statement means "if modulo 9 is 0, then return 9. Otherwise return modulo 9".
        
        also:
            739 % 9 == sum(700 % 9 + 30 % 9 + 9 % 9) if sum < 9 else sum % 9 
    """
#    return n%9 or n and 9 


print(digital_root(0))