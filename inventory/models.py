from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"
class Product(models.Model):
    name = models.CharField("product name",max_length=100, help_text="this is help text")
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    url = models.SlugField()
    is_active = models.BooleanField()
    category = models.ManyToManyField(Category)
    qty = models.IntegerField()

    def __str__(self):
        return self.name




class Brand(models.Model):
    name = models.CharField( max_length=100)


    def __str__(self):
        return self.name

class Stock(models.Model):
    units = models.BigAutoField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)