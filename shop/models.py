from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title


class Size(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size


class Color(models.Model):
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.color


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = (
        (GENDER_MALE, 'Male', ), 
        (GENDER_FEMALE, 'Female', ), 
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=GENDER_FEMALE)
    title = models.CharField(max_length=100)
    size = models.ManyToManyField(Size)
    color = models.ManyToManyField(Color)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    season = models.CharField(max_length=155)
    top_material = models.CharField(max_length=100)
    insole_material = models.CharField("Материал стельки", max_length=100)
    outsole_material = models.CharField("Материал подошвы", max_length=100)
    lining_material = models.CharField("Материал подкладки", max_length=100)
    type_outsole = models.CharField("Тип подошвы", max_length=100)
    fastening_method = models.CharField("Способ крепления", max_length=100)
    fullness = models.CharField("Полнота", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='image')
    name = models.CharField(max_length=40, null=True)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return f"{self.name} - {self.product.title}"



class Stock(models.Model):
    amount = models.PositiveIntegerField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    percent = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.title}: {self.amount}"


class Blog(models.Model):
    title = models.CharField(max_length=150)
    sub_title = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='blog/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Review(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
