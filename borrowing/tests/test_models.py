from django.test import TestCase

from ..models import User, Company, LoanRequest

# Create your tests here.

class UserModelsTest(TestCase):

    def test_string_representation(self):
        user = User(
            forename="Barry",
            surname="White",
            email="Barry.White@example.com",
            telephone_number="+441892000000",
            )
        self.assertEqual(str(user), "{0.surname}, {0.forename}".format(user),
                         "String representation incorrect for user")

class CompanyModelsTest(TestCase):

    def test_string_representation(self):
        company = Company(
            name="Green Light",
            address="1 The Street, Littlehaven, Hampshire",
            postcode="SO50 8RE",
            registered_company_number="12345678",
            business_sector=Company.ENTERTAINMENT,
            )
        self.assertEqual(str(company), company.name,
                         "String representation incorrect for company")

    def test_verbose_name_plural(self):
        self.assertEqual(str(Company._meta.verbose_name_plural), "companies")


class LoanRequestModelsTest(TestCase):

    def test_string_representation(self):
        loan_request = LoanRequest(
            amount=10000,
            loan_length_days=100,
            reason="I want to open another trendy cafe in Shoreditch",
            )
        self.assertEqual(
            str(loan_request),
            "borrowing: {0}".format(loan_request.amount),
            "String representation incorrect for loan request",
            )
