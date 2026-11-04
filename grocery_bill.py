rice_price = 45
sugar_price = 40
oil_price = 130

rice_quantity = 3
sugar_quantity = 2.5
oil_quantity = 1.8

rice_total = rice_quantity * rice_price
sugar_total = sugar_quantity * sugar_price
oil_total = oil_quantity * oil_price

print("Total cost of rice:", rice_total)
print("Total cost of sugar:", sugar_total)
print("Total cost of oil:", oil_total)

totalBill = rice_total + sugar_total + oil_total

print("Total bill:", totalBill)
print("Total bill as integer:", int(totalBill))
print("Total bill as string:", str(totalBill))

import random
deliveryCharge = random.randint(5, 10)
print("Delivery charge:", deliveryCharge)

finalBill = totalBill + deliveryCharge

print("Final amount:", finalBill)
print("Final amount as integer:", int(finalBill))
