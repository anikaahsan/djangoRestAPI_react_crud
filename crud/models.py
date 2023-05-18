from django.db import models

# Create your models here.
class Product(models.Model):
    status_choices=[
        ('In stock','In stock'),
        ('stockout','stockout')
    ]
    title=models.CharField(max_length=255,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    price=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    status=models.CharField(choices=status_choices,max_length=255,default='In stock')     

    # def __str__(self):
    #     return self.id                                                                  