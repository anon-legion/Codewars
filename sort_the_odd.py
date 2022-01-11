def sort_array(source_array):
  odd_nums = sorted([n for n in source_array if n % 2])
  return [n if not n % 2 else odd_nums.pop(0) for n in source_array]

# test = sort_array([])
# print(test)