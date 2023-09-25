from django.db import models

# Create your models here.

class Company(models.Model):
    company_name=models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class Product(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.product_name
