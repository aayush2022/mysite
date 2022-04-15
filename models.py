from django.db import models

class Books(models.Model):
    book_name = models.CharField(max_length=100)
    book_price = models.IntegerField()

    def __str__(self):
        return self.book_name        
    

class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer_name

