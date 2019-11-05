from django.db import models


class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    GoodsName = models.TextField(blank=True, null=True)
    GoodsPrice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
   
    class Meta:
        managed = True
        db_table = 'Goods'

	
class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    Goods = models.ForeignKey(Goods,models.SET_NULL, null=True)
    OrderDate = models.DateField(blank=True, null=True)
    	
    class Meta:
        managed = True
        db_table = 'Orders'
		
		
class User(models.Model):
    id = models.AutoField(primary_key=True)
    FirstName = models.TextField(blank=True, null=False)
    LastName = models.TextField(blank=True, null=False)
    BirthDate = models.DateField(blank=True, null=True)
    RegistrationDate = models.DateField(blank=True, null=False)
    Order = models.ForeignKey(Orders,models.SET_NULL, null=True)    	
    class Meta:
        managed = True
        db_table = 'User'