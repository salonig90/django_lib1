from django.db import models

# Model for Admin user
class Admin(models.Model):
    email = models.EmailField(unique=True)  # Ensure email is unique
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.email

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13, unique=True)
    
    def __str__(self):
        return self.title


