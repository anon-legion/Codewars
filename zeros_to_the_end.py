def move_zeros(arr):
  """
  Given an array of integers, move all the zeros to the end of the array.
  """
  non_zero_elements = [i for i in arr if i != 0]
  return non_zero_elements + [0 for i in range(len(arr) - len(non_zero_elements))]

# test = move_zeros([0, 0, 0, 0, 0, 0, 5, 3, 0, 0, 0, 3])
# print(test)