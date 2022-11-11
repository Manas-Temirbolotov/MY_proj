import json

from my_app.models import Customer, Work, Account


with open('data.json', 'r') as file:
	my_data = json.load(file)

for create in my_data:
	c = Customer(name=create['name'], phone=create['phone'], email=create['email'])
	c.save()
	w = Work(address=create['address'], city=create['city'], company=create['company'], postalZip=create['postalZip'], customer=c)
	w.save()
	a = Account(pin=create['pin'], acc_num=create['acc_num'], pan=create['pan'], cvv=create['cvv'], customer=c)
	a.save()

