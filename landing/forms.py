from django import forms
from .models import *
import hashlib


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ["is_active", "is_admin"]

    # шифрование пароля перед записью в базу
    def clean_password(self):
        data = self.cleaned_data["password"]
        data = bytes(data, encoding='UTF-8')
        data = hashlib.md5(data).hexdigest()
        print(data)
        return data


class DefenceForm(forms.ModelForm):
    class Meta:
        model = Defence
        exclude = ["def_id"]
