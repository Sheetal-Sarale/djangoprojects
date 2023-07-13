from django import forms
from.models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class GeeksForm(forms.Form):      # new form create karne ke liye
    title = forms.CharField()
    description = forms.CharField() 
    date_time = forms.DateTimeField()
    is_active = forms.BooleanField()
    price = forms.IntegerField()
    first_name = forms.CharField(max_length = 200) 
    last_name = forms.CharField(max_length = 200) 
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number") 
    password = forms.CharField(widget = forms.PasswordInput())


class BookForm(forms.ModelForm):
    class Meta():
        model = Book
        fields = '__all__'
        exclude = ('is_active'),                       # exclude any field or delete any field

STATES = (
    ('', 'Choose...'),
    ('MH', 'Maharashtra'),
    ('AP', 'AndhraPradesh'),
    ('UP', 'UttarPradesh')
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(label='Address',widget=forms.TextInput(attrs={'placeholder': '1234 Main St'}))
    address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'}))
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)
