from django.db import models

# Create your models here.
class Filter(models.Model):
    class Colour(models.TextChoices):
        BROWN = 'brown', "Jigar rang"
        RED = 'red', 'Qizil rang'
        GREEN = 'green', 'Yashil rang'
        BLUE = 'blue', "Ko'k rang"
        BLACK = 'black', 'Qora rang'
        WHITE = 'white', 'Oq rang'
        GOLDEN = 'golden', 'Oltin rang'
        
    class Brand(models.TextChoices):
        ADIDAS = 'adidas', 'Adidas'
        NIKE = 'nike', 'Nike'
        CHANEL = 'chanel', 'Chanel'
        GUCCI = 'gucci', 'Gucci'
        PRADA = 'prada', 'Prada'

    in_trend = models.BooleanField(default=False)
    is_cheaper = models.BooleanField(default=False)
    is_expensive = models.BooleanField(default=False)
    in_top = models.BooleanField(default=True)
    is_new = models.BooleanField(default=True)
    is_original = models.BooleanField(default=True)
    top_deliveried = models.BooleanField(default=True)
    colour = models.CharField(max_length=100, choices=Colour.choices)
    brand = models.CharField(max_length=100, choices=Brand.choices)
    price = models.PositiveIntegerField(default=0)


class Basket(models.Model):
    class Pay(models.TextChoices):
        CARD = 'card', "Karta orqali"
        SUMM = 'summ', "Naqd pul orqali"    
    products = models
    amount = models.PositiveIntegerField(default=0)
    total_price = models.PositiveIntegerField(default=0)
    joined_at = models.DateField(auto_created=True)
    pay_with = models.CharField(max_length=100, choices=Pay.choices)


class ForMen(models.Model):
    kiyimlar = models 


class Category(models.Model):
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    erkaklar_uchun = models.BooleanField()
    if erkaklar_uchun == True:
        print()
    ayollar_uchun = models.BooleanField()
    bolalar_uchun = models.BooleanField()
    