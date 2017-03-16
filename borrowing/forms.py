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


class LoanRequestForm(forms.ModelForm):
    class Meta:
        model = LoanRequest
        fields = ["amount", "loan_length_days", "reason"]