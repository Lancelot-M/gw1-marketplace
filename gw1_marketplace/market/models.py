from django.db import models

class Category(models.Model):
    """Category to organize items"""
    name = models.CharField(max_length=100, unique=True)
    category_parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name


class SellOrder(models.Model):
    """Sell oder of X items"""
    item = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    total_unit = models.IntegerField()
    total_price = models.IntegerField()
    money_used = models.CharField(max_length=100)
    seller = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    class Meta:
        ordering = ["item", "total_unit", "total_price"]
    
    def __str__(self):
        return self.item

