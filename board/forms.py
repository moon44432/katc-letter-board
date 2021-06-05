from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=40, widget=forms.TextInput({
        'class': 'compose-title',
        'placeholder': '제목 (보내는 이의 이름을 포함해 주세요)',
    }))
    content = forms.CharField(widget=forms.Textarea({
        'id': 'editor',
        'placeholder': '답장을 받기 위해서는 주소와 우편번호를 반드시 적어 주세요.',
    }))


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
