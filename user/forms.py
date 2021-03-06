from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from user.models import Profile


def ForbiddenUsers(value):
    forbidden_users = ['admin', 'css', 'js', 'authenticate', 'login', 'logout', 'administrator', 'root',
                       'email', 'user', 'join', 'sql', 'static', 'python', 'delete']
    if value.lower() in forbidden_users:
        raise ValidationError('사용할 수 없는 아이디 입니다.')


def InvalidUser(value):
    if '@' in value or '+' in value or '-' in value:
        raise ValidationError('사용할 수 없는 문자가 포함되어 있습니다: @ , - , + ')


def UniqueEmail(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('이미 사용중인 이메일 입니다.')


def UniqueUser(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('이미 사용중인 아이디 입니다.')


class SignupForm(forms.ModelForm):

    username = forms.CharField(
        widget=forms.TextInput(), max_length=30, required=True)
    email = forms.CharField(widget=forms.EmailInput(),
                            max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(), required=True, label="비밀번호를 확인해 주세요.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(ForbiddenUsers)
        self.fields['username'].validators.append(InvalidUser)
        self.fields['username'].validators.append(UniqueUser)
        self.fields['email'].validators.append(UniqueEmail)

    def clean(self):
        super(SignupForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            self._errors['password'] = self.error_class(
                ['비밀번호가 다릅니다. 다시 입력해주세요'])

        return self.cleaned_data


class ChangePasswordform(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    old_password = forms.CharField(
        widget=forms.PasswordInput(), label="Old password", required=True)
    new_password = forms.CharField(
        widget=forms.PasswordInput(), label="New password", required=True)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(), label="Confirm new password", required=True)

    class Meta:
        model = User
        fields = ('id', 'old_password', 'new_password', 'confirm_password')

    def clean(self):
        super(ChangePasswordform, self).clean()
        id = self.cleaned_data.get('id')
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        user = User.objects.get(pk=id)
        if not user.check_password(old_password):
            self._errors['old_password'] = self.error_class(
                ['Old password do not match.'])
        if new_password != confirm_password:
            self._errors['new_password'] = self.error_class(
                ['Passwords do not match.'])
        return self.cleaned_data

class EditProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=True)
    name = forms.CharField(widget=forms.TextInput(), max_length=30, required=True)
    url = forms.URLField(widget=forms.TextInput(), max_length=30, required=False)
    profile_info = forms.CharField(widget=forms.TextInput(), max_length=260, required=False)

    class Meta:
        model = Profile
        fields = ('picture', 'name', 'url', 'profile_info')
