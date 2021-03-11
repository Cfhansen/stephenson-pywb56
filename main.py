print("Enter number of minutes and texts:")
minutes, texts = input().split(',')
minutes = int(minutes)
texts = int(texts)

base_charge = 15.0
minutes_charge = 0
if minutes > 50:
  minutes_charge += .25 * (minutes - 50)
texts_charge = 0
if texts > 50:
  texts_charge += .15 * (texts - 50)
charge_911 = 0.44
tax = 0.05 * (base_charge + minutes_charge + texts_charge + charge_911)
tax = round(tax,2)

print(f"""Base fee: {base_charge}. 
911 fee:  {charge_911}. 
Tax:      {tax}. """)
if minutes_charge:
  print(f'Minutes overage fee: {minutes_charge:.2f}.')
if texts_charge:
  print(f'Texts overage fee: {texts_charge:.2f}.')
print(f'Total fee: {base_charge + minutes_charge + texts_charge + charge_911 + tax}.')
