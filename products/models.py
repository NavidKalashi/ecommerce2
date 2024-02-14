from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image
    description = models.TextField()

    def __str__(self):
        return self.product_name