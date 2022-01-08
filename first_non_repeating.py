def first_non_repeating_letter(string):
  no_repeat_chars = [i for i in string if string.lower().count(i.lower()) == 1]
  return no_repeat_chars[0] if unique_chars else ''

# test = first_non_repeating_letter('moonmen')
# print(test)