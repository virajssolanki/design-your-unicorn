from django import forms
from .models import Uimg


class UimgForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(max_length = 200)
    designation = forms.CharField(required=False) 
    company_name = forms.CharField(required=False)
    commitment_1 = forms.CharField(required=False)
    commitment_2 = forms.CharField(required=False)
    img = forms.ImageField()
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(UimgForm, self).__init__(*args, **kwargs)
        self.fields['img'].label = "Upload a Photo"
        self.fields['commitment_1'].label = "I commit myself to generate Rs. ______ revenues"
        self.fields['commitment_2'].label = "I commit myself to generate ______ Jobs "