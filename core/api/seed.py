from faker import Faker 
from .models import *
import random
fake=Faker()

def seed_db(n):
    try:
        for _ in range(0,n):
            company_obj=Company.objects.all()
            comp_idx=random.randint(0,len(company_obj)-1)
            company=company_obj[comp_idx]
            product_name=fake.name()
            price=random.randint(100,10000)
            description=fake.text()

            product_obj=Product.objects.create(company=company,product_name=product_name,price=price,description=description)
    except Exception as e:
        print(e)