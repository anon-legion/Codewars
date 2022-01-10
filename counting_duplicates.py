def duplicate_count(text):
  return len([i for i in set(text.lower()) if text.lower().count(i) > 1])

# test_string = 'aaawwgt'
# test = duplicate_count(test_string)
# print(test)
