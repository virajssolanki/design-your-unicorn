from django import forms
from .models import Uimg


SITES = (
    ('  ', '    '),
    ('ડાભોર', 'ડાભોર'),
    ('તાંતિવેલા', 'તાંતિવેલા'),
    ('છાત્રોડા', 'છાત્રોડા'),
    ('ડારી', 'ડારી'),
    ('દેદા', 'દેદા'),
    ('પાલડી', 'પાલડી'),
    ('છાપરી', 'છાપરી'),
    ('હસ્નાવદર', 'હસ્નાવદર'),
    ('મલોંઢા', 'મલોંઢા'),
    ('ખેરાળી', 'ખેરાળી'),
    ('વાવડી', 'વાવડી'),
    ('ચમોડા ', 'ચમોડા'),
    ('સારસવા ', 'સારસવા'),
    ('કીંદરવા ', 'કીંદરવા'),
    )

class UimgForm(forms.Form):
    name = forms.CharField(required=False)
    village = forms.ChoiceField(choices = SITES) 
    number = forms.CharField(required=False)
    img = forms.ImageField()
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(UimgForm, self).__init__(*args, **kwargs)
        self.fields['img'].label = "ફોટો પસંદ કરવા માટે નીચેનું બટન દબાવો"
        self.fields['name'].label = "તમારું નામ"
        self.fields['number'].label = "મોબાઇલ નંબર"
        self.fields['village'].label = "તમારું ગામ"