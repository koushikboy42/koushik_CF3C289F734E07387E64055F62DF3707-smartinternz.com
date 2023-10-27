def linear_search_product(products, target_product):
  indices = []

  for index, product in enumerate(products):
      if product == target_product:
          indices.append(index)

  return indices

# Example usage:
product_list = ["Apple", "Banana", "Apple", "Orange", "Apple", "Mango"]
target = "Apple"
result = linear_search_product(product_list, target)

if result:
  print(f"{target} found at indices: {result}")
else:
  print(f"{target} not found in the product list.")
