from django import forms
class myForm(forms.Form):
    interger = forms.IntegerField(label='Interger Field')
    character = forms.CharField(label='Character Field',widget=forms.TextInput(attrs={'class':'asdasdf'}))
    date = forms.DateField(label='Date Field',widget=forms.DateInput(attrs={'type':'date'}))
    radio = forms.ChoiceField(choices=[('one','one'),('two','two'),('three','thhree')],widget=forms.RadioSelect(),label='Radio Field')
    textarea = forms.CharField(label='TextArea',widget=forms.Textarea())
    checkbox = forms.BooleanField(label='Checkbox Field')
    select = forms.ChoiceField(choices=[('a','a'),('b','b'),('c','c')],widget=forms.Select(),label='Select Field')
    file = forms.FileField(label='File Field')
    button = forms.CharField(widget=forms.TextInput(attrs={'type':'button','value':'submit'}))