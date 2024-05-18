# forms.py

from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']


class BookingForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    datetime = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control datetimepicker-input', 'placeholder': 'Date & Time', 'data-target': '#date3', 'data-toggle': 'datetimepicker'}))
    people = forms.ChoiceField(choices=[(1, 'People 1'), (2, 'People 2'), (3, 'People 3')], widget=forms.Select(attrs={'class': 'form-select'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Special Request', 'style': 'height: 100px'}), required=False)