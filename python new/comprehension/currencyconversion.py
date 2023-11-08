print("CURRENCY CONVERSION")
print("=================================")

print({num:"num" for num in range(1,5)})

price={'milk':2,"cookies":3,'tea':3}
dhm_inr=20
# for i in price.items():
#     print(i)
new_price={item:value*20 for item,value in price.items() }
print(new_price)