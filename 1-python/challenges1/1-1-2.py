x = int(input("check"))
tip = int(input("tip %"))
number = int(input("number of diners"))

tip = tip/100
total_tip = x*number*tip
total_amount = total_tip+x

per_person = total_amount/number

print(f"total amout:$ {x:.2f}")
print(f"total tips:$ {total_tip:.2f}")
print(f"total amout with tips:$ {total_amount:.2f}")
print(f"perperson$ {per_person:.2f}")