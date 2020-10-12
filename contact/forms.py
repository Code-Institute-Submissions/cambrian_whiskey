from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'contact-form-input'}))

    email_address = forms.EmailField(required=True, widget=forms.EmailInput(attrs=
      {'class':'contact-form-input'}))

    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'contact-form-input'}))

    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class':'contact-form-input'})
    )

    class Meta:
        model = Contact
        fields = [
            'name', 'subject', 'email_address', 'message'
        ]

