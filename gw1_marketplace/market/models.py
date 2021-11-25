from django.db import models

class Group(models.Model):
    """Group of categories"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    """Category to organize items"""
    name = models.CharField(max_length=100, unique=True)
    group_parent = models.ForeignKey(Group, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class SellOrder(models.Model):
    """Sell oder of X items"""
    item = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    total_unit = models.IntegerField()
    total_price = models.IntegerField()
    money_used = models.CharField(max_length=50)
    seller = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    class Meta:
        ordering = ["item", "total_unit", "total_price"]
    
    def __str__(self):
        return self.item

