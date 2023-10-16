from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm, UsernameField,
                                       PasswordChangeForm, SetPasswordForm, PasswordResetForm)
from django import forms
from django.contrib.auth.models import User

from .models import Customer


class LoginForm(AuthenticationForm):
    username = UsernameField(label='Tài khoản', widget=forms.TextInput(attrs={'autofocus': 'True',
                                                                              'class': 'form-control'}))
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                                                                   'class': 'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Tài khoản', widget=forms.TextInput(attrs={'autofocus': 'True',
                                                                                'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Mật khẩu cũ', widget=forms.PasswordInput(
        attrs={'autofocus': 'True', 'autocomplete': 'current-password', 'class': 'form-control'}))
    new_password1 = forms.CharField(label='Mật khẩu mới', widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))
    new_password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label='Mật khẩu mới', widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))
    new_password2=forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))
class CustomerProfileForm(forms.ModelForm):
    name = forms.CharField(label='Họ và tên', widget=forms.TextInput(attrs={'autofocus': 'True',
                                                                                'class': 'form-control'}))
    locality = forms.CharField(label='Địa chỉ chi tiết', widget=forms.TextInput(attrs={'autofocus': 'True',
                                                                                'class': 'form-control'}))
    city = forms.CharField(label='Thành phố', widget=forms.TextInput(attrs={'autofocus': 'True',
                                                                                'class': 'form-control'}))
    mobile = forms.CharField(label='Số điện thoại', widget=forms.NumberInput(attrs={'autofocus': 'True',
                                                                                'class': 'form-control'}))
    zipcode = forms.CharField(label='Mã zip', widget=forms.NumberInput(attrs={'autofocus': 'True',
                                                                                'class': 'form-control'}))
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'mobile', 'zipcode']

