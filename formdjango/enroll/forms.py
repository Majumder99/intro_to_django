from django import forms


class StudentRegistratoinForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    # password = forms.CharField(widget=forms.PasswordInput)
    # re_password = forms.CharField(widget=forms.PasswordInput)
    # class_attr = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # date_type = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


    # def clean(self):
    #     cleaned_data = super().clean()
    #     valpwd = cleaned_data.get('password')
    #     valrpwd = cleaned_data.get('re_password')
    #     if valpwd != valrpwd:
    #         raise forms.ValidationError('Password and Confirm Password not matched')
    #     return cleaned_data