from django import forms
from .models import Uimg


class UimgForm(forms.Form):
    name = forms.CharField(required=False)
    village = forms.ChoiceField(required=False) 
    number = forms.CharField(required=False)
    img = forms.ImageField()
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(UimgForm, self).__init__(*args, **kwargs)
        self.fields['img'].label = "Upload a Photo"
        self.fields['name'].label = "Name"
        self.fields['number'].label = ""
        self.fields['village'].label = "Email"