product_price = int(input("What is the price of the product"))

if product_price < 100:
  discount = product_price * 0.02

else:
  discount = product_price * 0.10

net_price = product_price - discount

print("Product Price:" , net_price)



