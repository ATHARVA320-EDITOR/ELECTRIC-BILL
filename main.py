units = int(input("Enter units consumed"))
if(units <= 50):
    amount = units * 2.60
    tax = 25
elif(units<=100):
    amount = 130 + ((units - 50)* 3.25)
    tax = 50
elif(units<=200):
    amount = 130 + 162.50 + ((units - 100)* 5.26)
    tax = 50
else:
    amount = 130 + 162.50 + 526 + ((units - 200)* 8.45)
    tax = 75
total = amount + tax
print("\nElectricity Bill = %.2f" %total)