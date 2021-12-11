from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['email','password','password_2']

        labels = {
            'email':'Email Id',
            'password':'Password',
        }


        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control'}),            
        }

    
    def clean_email(self):
        '''
        Verify email is available.
        '''
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data



class AuthenticationForm(forms.Form): 
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'text','name': 'email','placeholder':'Email'}), 
        label='Email')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','type':'password', 'name': 'password','placeholder':'Password'}),
        label='Password')

    class Meta:
        fields = ['email', 'password']