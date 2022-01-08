def move_zeros(arr):
  """
  Given an array of integers, move all the zeros to the end of the array.
  """
  return [i for i in arr if i] + [i for i in arr if not i]

# test = move_zeros([0, 8, 0, 0, 0, 0, 1, 1])
# print(test)