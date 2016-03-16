from django import forms
from django.contrib.auth.models import User

from qa.models import Question, Answer
from django.contrib.auth.forms import UserCreationForm


class AskForm(forms.Form):
    title = forms.CharField(max_length=300, widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def clean(self):
        if self.user.is_anonymous():
            raise forms.ValidationError("Not Autorized", code="not_auth")
        return self.cleaned_data

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = self.user.id
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    question = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'form-control'}))

    def clean(self):
        if self.user.is_anonymous():
            raise forms.ValidationError("Not Autorized", code="not_auth")
        return self.cleaned_data

    def save(self):
        self.cleaned_data['question'] = Question(self.cleaned_data['question'])
        answer = Answer(**self.cleaned_data)
        answer.author_id = self.user.id
        answer.save()
        return answer


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")
