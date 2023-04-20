from django import forms

class AnswerForm(forms.Form):
    answer_text = forms.CharField(max_length=200, widget=forms.Textarea,label='Answer :')
