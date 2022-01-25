'''
  Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
  The function should return true if the string is valid, and false if it's invalid.
  Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters.
  Furthermore, the input string may be empty and/or not contain any parentheses at all.
  Do not treat other forms of brackets as parentheses (e.g. [], {}, <>)
'''

def valid_parentheses(string, pointer=0):
  paren_string = ''.join([s for s in string if s in '()'])
  # if all parenthesis are matched, return True
  if len(paren_string) == 0:
    return True
  # if there are unmatched parenthesis, return False
  if len(paren_string) == pointer + 1:
    return False
  # if is pair, prune the pair reset pointer and call again
  if paren_string[pointer] == '(' and paren_string[pointer + 1] == ')':
    return valid_parentheses(paren_string[:pointer] + paren_string[pointer + 2:], pointer=0)
  # if not pair, move pointer to next index and call again
  else:
    return valid_parentheses(paren_string, pointer = pointer + 1)

def valid_parentheses_2(string):
  paren_string = ''.join([s for s in string if s in '()'])
  while '()' in paren_string:
    paren_string = paren_string.replace('()', '')
  return not paren_string

# test_string = 'hi(hi)()'
# test_output = valid_parentheses(test_string)
# print(test_output)