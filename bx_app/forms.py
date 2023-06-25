from django import forms

class AnswerForm(forms.Form):
    answer_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 12, 'cols': 75}),label='')
