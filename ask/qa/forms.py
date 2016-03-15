from django import forms

from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = 1
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    question = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'form-control'}))

    def save(self):
        self.cleaned_data['question'] = Question(self.cleaned_data['question'])
        answer = Answer(**self.cleaned_data)
        answer.author_id = 1
        answer.save()
        return answer
