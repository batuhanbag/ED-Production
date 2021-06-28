from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.db.models import fields


from account.models import Account


class RegistrationForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = Account
        fields = ("email", "fullName", "password1", "password2",
                  "universty", "department", "account_type")


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):

        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Giriş Başarısız.")


class AccountUptadeForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('email', 'fullName', 'universty',
                  'department', 'account_type', 'account_avatar')

        def clean_email(self):
            email = self.cleaned_data['email']
            fullName = self.cleaned_data['fullName']
            universty = self.cleaned_data['University']
            department = self.cleaned_data['Department']
            account_type = self.cleaned_data['account_type']
            account_avatar = self.cleaned_data['account_avatar']
            try:
                account = Account.objects.exclude(
                    pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Bu Email "%s" kullanılıyor' % account)


class UserDeleteForm(forms.ModelForm):

    class Meta:
        model = Account

        fields = []
