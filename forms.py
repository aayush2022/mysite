from django import forms
from . models import Books, Customer

class Booksform(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"

class Customerform(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"











