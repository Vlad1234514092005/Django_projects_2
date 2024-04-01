from .models import Book
from django.forms import TextInput, ModelForm, Textarea, IntegerField


class BookAddForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'publishing_date', 'genre', 'description']