from django.db import models

class Category:
    name = models.CharField(max_length=266)

    def __str__(self):
        return self.name
    
class Product:
    title = models.CharField(max_length=100)
    decrtiption = models.CharField(max_length=250)
    price = models.IntegerField()
    category = models.ForeignKey()

    def __str__(self):
        return self.title, self.decrtiption, self.price, self.category
    
class Review:
    text = models.CharField(max_length=266)
    product = models.ForeignKey()

    def __str__(self):
        return self.text, self.product