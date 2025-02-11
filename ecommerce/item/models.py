from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        db_table = ''
        ordering = ['name']
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey('Category', related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_image', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    
    class Meta:
        db_table = ''
        ordering = ['name']
        managed = True
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        
    def __str__(self):
        return self.name