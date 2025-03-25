from django import forms

class login_form(forms.Form):
    user = forms.CharField(max_length=50, label='User', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control rounded-0',
        'placeholder': 'User',
        
    }))
    password = forms.CharField(max_length=100,label='Password',widget=forms.PasswordInput(attrs={
        'class': 'form-control rounded-0',
        'placeholder': 'Password',
    }))