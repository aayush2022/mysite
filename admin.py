from django.contrib import admin
from . models import Customer, Books

admin.site.register(Books)
admin.site.register(Customer)

