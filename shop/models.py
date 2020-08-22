from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=100, default="")
    sub_category = models.CharField(max_length=100,default="")
    description = models.CharField(max_length=1056)
    published_date = models.DateTimeField(auto_now_add=True)
    product_image = models.ImageField(upload_to='product_image', default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.product_name