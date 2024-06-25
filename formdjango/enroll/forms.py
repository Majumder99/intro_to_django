from django import forms


class StudentRegistratoinForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)
    # re_password = forms.CharField(widget=forms.PasswordInput)


    # def clean(self):
    #     cleaned_data = super().clean()
    #     valpwd = cleaned_data.get('password')
    #     valrpwd = cleaned_data.get('re_password')
    #     if valpwd != valrpwd:
    #         raise forms.ValidationError('Password and Confirm Password not matched')
    #     return cleaned_data