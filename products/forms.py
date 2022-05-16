import email
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='', widget=forms.Textarea(
        attrs={
            "id": "id-title",
            "placeholder": "Your description"
        }
    ))
    email       = forms.EmailField()
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            "class":"class-name one",
            "placeholder": "Your description",
            "id": "id-desc",
            "rows": 20,
            "cols": 120
        }
    ))
    price       = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not "django" in title:
            raise forms.ValidationError("This is not a valid title")
        return title
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email
                      

class RawProductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.Textarea(
        attrs={
            "id": "id-title",
            "placeholder": "Your description"
        }
    ))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            "class":"class-name one",
            "placeholder": "Your description",
            "id": "id-desc",
            "rows": 20,
            "cols": 120
        }
    ))
    price       = forms.DecimalField(initial=199.99)