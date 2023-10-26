from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field

from .models import tbl_Companydetails

class Companymaster(forms.ModelForm):
    class Meta:
        model = tbl_Companydetails
        fields=['companyName','Address','contactNo','establisheddate','websitelink','emailaddress']
