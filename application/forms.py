
from django import forms
from .models import Customer 
from .models import  Lead
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'  