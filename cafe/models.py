from django.db import models

# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=125)
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=125)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.email} {self.create_at}"