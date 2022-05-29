ruble=3
kopek=11
amount=5

print(round((ruble+kopek/100)*amount,2))
print((ruble*100+kopek)*amount)
print("price=", ruble*amount,"rub.",kopek*amount,"kop.")

print("price= {} rub. {} kop.".format(ruble*amount,kopek*amount))