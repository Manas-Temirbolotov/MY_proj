from django.db.models import Subquery, Q
from my_app.models import Customer, Work, Account

customers = Customer.objects.filter(email__icontains='icloud.com')
print(customers)

customer_company = Customer.objects.filter(work__company__icontains='Ltd')
print(customer_company)

account = Account.objects.filter(customer__email__icontains='protonmail')
print(account)
