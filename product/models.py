from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=266)
    

    def __str__(self):
        return self.name
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    decrtiption = models.CharField(max_length=250)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title, self.decrtiption, self.price, self.category
STARS = (
    (i, '*' * i)for i in range(1, 6)
    )
    
class Review(models.Model):
    text = models.CharField(max_length=266)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=STARS, default=5)
    def __str__(self):
        return self.text, self.product