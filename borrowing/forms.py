from django import forms

from .models import User, Company, LoanRequest


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["forename", "surname", "email", "telephone_number"]

    def clean_telephone_number(self):
        """method to validate the minimum length of the telephone number"""
        data = self.cleaned_data["telephone_number"]
        if len(data) < 7:
            raise forms.ValidationError("telephone number must be at least 7 "
                                        "characters long")
        return data


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