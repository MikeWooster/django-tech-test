from django import forms
from django.contrib.auth.models import User as UserAuth

from .models import User, Company, LoanRequest


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["forename", "surname", "email", "telephone_number"]
        exclude = ["userauth"]

    def __init__(self, *args, **kwargs):
        """Override init to enable setting company to default None"""
        self.company = None
        self.userauth = None
        super().__init__(*args, **kwargs)

    def clean_telephone_number(self):
        """method to validate the minimum length of the telephone number"""
        data = self.cleaned_data["telephone_number"]
        if len(data) < 7:
            raise forms.ValidationError("telephone number must be at least 7 "
                                        "characters long")
        return data

    def save(self):
        """Override save to set company foreign key"""
        user = super().save(commit=False)
        if isinstance(self.company, Company):
            user.company = self.company
        if isinstance(self.userauth, UserAuth):
            user.userauth = self.userauth
        user.save()
        return user

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name", "address", "postcode", "registered_company_number",
                  "business_sector"]

    def clean_registered_company_number(self):
        """
        method to validate that the length of the registered company number
        is 8 characters exactly
        """
        data = self.cleaned_data["registered_company_number"]
        if len(data) != 8:
            raise forms.ValidationError("registered company number must be "
                                        "exactly 8 characters")
        return data

class LoanRequestForm(forms.ModelForm):
    class Meta:
        model = LoanRequest
        fields = ["amount", "loan_length_days", "reason"]

    def __init__(self, *args, **kwargs):
        """Override init to enable setting company to default None"""
        self.company = None
        super().__init__(*args, **kwargs)

    def save(self):
        """Override save to set company foreign key"""
        loanrequest = super().save(commit=False)
        if isinstance(self.company, Company):
            loanrequest.company = self.company
        loanrequest.save()
        return loanrequest


class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)