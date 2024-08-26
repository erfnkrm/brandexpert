from django import forms
from .models import Contact
import gspread

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'source']


def G_sheet(name,email,phone,source):
    sa = gspread.service_account('/Users/Erfan/Workspace/brandexpert/BrandexpertApp/secret_key.json')
    sh = sa.open("Clients")
    wks = sh.worksheet('Data')
    row = [name, email, phone, source]
    wks.append_row(row)
