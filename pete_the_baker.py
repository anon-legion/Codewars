from math import floor as f

def cakes(recipe, available):
  return f(min([available.get(key, 0) / val for key, val in recipe.items()]))

# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
# print(cakes(recipe, available))