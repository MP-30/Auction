from django.db import models
from django.utils import timezone

class Item(models.Model):
    ITEM_CATEGORY_CHOICES = (
        ('group1', 'Group 1'),
        ('group2', 'Group 2'),
        # Add more groups as needed
    )

    SUB_CATEGORY_CHOICES = (
        ('category1', 'Category 1'),
        ('category2', 'Category 2'),
        # Add more categories as needed
    )

    item_code = models.CharField(max_length=20, unique=True)
    item_name = models.CharField(max_length=255)
    item_category = models.CharField(max_length=255, choices=ITEM_CATEGORY_CHOICES)
    standard_buying_rate = models.DecimalField(max_digits=10, decimal_places=2)
    standard_selling_rate = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    uom = models.CharField(max_length=255)
    item_subcategory = models.CharField(max_length=255, choices=SUB_CATEGORY_CHOICES)
    hsn_code = models.CharField(max_length=255)
    description = models.TextField()
    warehouse = models.CharField(max_length=255)

    def __str__(self):
        return self.item_name