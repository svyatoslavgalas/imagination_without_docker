from django import forms

from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=256)
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    email = forms.EmailField(
        label='Email',
        error_messages={
            'unique': 'Ошибка регистрации, данный E-mail уже используется'
        },
    )

    class Meta:
        model = User
        fields = ('email',)

    def save(self, request=None, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data["password"]
        user.set_password(password)
        if commit:
            user.save()
        return user
