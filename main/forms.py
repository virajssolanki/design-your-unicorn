from django import forms
from .models import Uimg, Choice, Question

CHOICES = (('item_key1', 'Item title 1.1'),
          ('item_key2', 'Item title 1.2'),
          ('item_key3', 'Item title 1.3'),
          ('item_key4', 'Item title 1.4'),
          ('item_key5', 'Item title 1.5'))

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

    qustion_1 = forms.ChoiceField(choices=CHOICES, 
        widget=forms.RadioSelect(), required=False, 
        label='Are you aware on how to evaluate the startup on these checklist points ?')

    def __init__(self, *args, **kwargs):
        super(UimgForm, self).__init__(*args, **kwargs)
        self.fields['img'].label = "Upload a Photo"
        self.fields['commitment_1'].label = "I commit myself to generate Rs. ______ revenues"
        self.fields['commitment_2'].label = "I commit myself to generate ______ Jobs "


class QuizForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        choice_list = tuple((x.percentage, x.choice ) for x in Choice.objects.filter(question=question).all())
        self.fields["answer"] = forms.ChoiceField(choices=choice_list, widget=forms.RadioSelect(), 
                                                    required=False, 
                                                    label=question.question)

class BaseQuizFormSet(forms.BaseFormSet):
    def get_form_kwargs(self, index):
        kwargs = super().get_form_kwargs(index)
        q = kwargs['questions'][index]
        return {'question': q}


