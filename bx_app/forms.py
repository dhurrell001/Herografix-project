from django import forms

class AnswerForm(forms.Form):
    answer_text = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'rows': 8, 'cols': 75}),label='')
