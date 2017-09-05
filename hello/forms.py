from django import forms

class RecordForm(forms.Form):
    way = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'有氧/力量','aria-describedby':'basic-addon1'}))
    strength = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'时间/组数','aria-describedby':'basic-addon2'}))