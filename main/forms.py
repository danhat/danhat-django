from django import forms
from .models import Messages

from phonenumber_field.modelfields import PhoneNumberField



class ContactForm(forms.ModelForm):

  name = forms.CharField(label='Name', max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': 'Enter Your Name...',
			'class': 'form-control'
			}))
  email = forms.EmailField(label='Email', max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': 'Enter Your Email...',
			'class': 'form-control'
			}))
  phone_number = forms.CharField(max_length=15, required = False,
    widget = forms.TextInput(attrs={
			'placeholder': 'Enter Your Phone Number...',
			'class': 'form-control'
			}))
  message = forms.CharField(label='Message', max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': 'Enter Your Message...',
			'class': 'form-control',
			'rows': 6,
			}))


  class Meta:
    model = Messages
    fields = ('name', 'email', 'phone_number', 'message',)
    # fields = ('name', 'email', 'message',)