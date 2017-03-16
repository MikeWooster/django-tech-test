from django.test import TestCase
from ..models import Company
from ..forms import UserForm, CompanyForm, LoanRequestForm


class UserFormTest(TestCase):
    def setUp(self):
        # Define attributes for consistent usage across tests
        self.forename = "Mike"
        self.surname = "Wooster"
        self.email = "Mike.Wooster@example.com"
        self.tel_no = "+441732777666"
        # Initialise a company object
        self.company = Company.objects.create(
            name="White Glass",
            address="213 Fake Street, Newhaven",
            postcode="UN48 8DF",
            registered_company_number="12345678",
            business_sector=Company.RETAIL
            )

    def test_valid(self):
        """Test if a submission of correct data works"""
        form = UserForm({
            "forename": self.forename,
            "surname": self.surname,
            "email": self.email,
            "telephone_number": self.tel_no,
            })
        self.assertTrue(form.is_valid(), "Form submission unsuccessful")

    def test_commit(self):
        """Tests successful save to db"""
        form = UserForm({
            "forename": self.forename,
            "surname": self.surname,
            "email": self.email,
            "telephone_number": self.tel_no,
        })
        form.company = self.company
        user = form.save()
        self.assertEqual(user.forename, self.forename)
        self.assertEqual(user.surname, self.surname)
        self.assertEqual(user.email, self.email)
        self.assertEqual(user.telephone_number, self.tel_no)
        self.assertEqual(user.company, self.company)

    def test_missing_fields(self):
        form = UserForm({})
        self.assertFalse(
            form.is_valid(),
            "Form with missing information needs to fail")
        self.assertEqual(
            form.errors,
            {"forename": ["This field is required."],
             "surname": ["This field is required."],
             "email": ["This field is required."],
             "telephone_number": ["This field is required."]},
            "Unexpected response in errors with missing fields"
            )

    def test_telephone_number_too_short(self):
        form = UserForm({
            "forename": self.forename,
            "surname": self.surname,
            "email": self.email,
            "telephone_number": "076524",
            })
        self.assertFalse(form.is_valid(),
                         "Telephone number must be at least 7 digits long")

    def test_telephone_number_too_long(self):
        form = UserForm({
            "forename": self.forename,
            "surname": self.surname,
            "email": self.email,
            "telephone_number": "01892038474939743",
            })
        self.assertFalse(form.is_valid(),
                         "Telephone number must be a maximum of 15 digits")

    def test_invalid_email(self):
        form = UserForm({
            "forename": self.forename,
            "surname": self.surname,
            "email": "Mike@",
            "telephone_number": self.tel_no,
            })
        self.assertFalse(form.is_valid(),
                         "Invalid email was incorrectly validated")

class CompanyFormTest(TestCase):
    def setUp(self):
        # Define attributes for consistent usage across tests
        self.name = "White Glass"
        self.address = "123 Fake Street, London"
        self.postcode = "SW2 4DF"
        self.registered_company_number = "12345678"
        self.business_sector = Company.RETAIL

    def test_valid(self):
        form = CompanyForm({
            "name": self.name,
            "address": self.address,
            "postcode": self.postcode,
            "registered_company_number": self.registered_company_number,
            "business_sector": self.business_sector
            })
        self.assertTrue(form.is_valid(), "CompanyForm submission failed")
        company = form.save()
        self.assertEqual(company.name, self.name)
        self.assertEqual(company.address, self.address)
        self.assertEqual(company.postcode, self.postcode)
        self.assertEqual(
            company.registered_company_number, self.registered_company_number
            )
        self.assertEqual(company.business_sector, self.business_sector)

    def test_missing_fields(self):
        form = CompanyForm({})
        self.assertFalse(
            form.is_valid(),
            "Form with missing information needs to fail")
        self.assertEqual(
            form.errors,
            {"name": ["This field is required."],
             "address": ["This field is required."],
             "postcode": ["This field is required."],
             "registered_company_number": ["This field is required."],
             "business_sector": ["This field is required."]},
            "Unexpected response in errors with missing fields"
            )

    def test_registered_company_number_too_long(self):
        form = CompanyForm({
            "name": self.name,
            "address": self.address,
            "postcode": self.postcode,
            "registered_company_number": "123456789",
            "business_sector": self.business_sector
        })
        self.assertFalse(
            form.is_valid(),
            ("Expecting form with registered company number over 8 characters "
             "to fail")
            )

    def test_registered_company_number_too_short(self):
        form = CompanyForm({
            "name": self.name,
            "address": self.address,
            "postcode": self.postcode,
            "registered_company_number": "1234567",
            "business_sector": self.business_sector
            })
        self.assertFalse(
            form.is_valid(),
            ("Expecting form with registered company number under 8 "
             "characters to fail")
            )

    def test_business_sector_valid(self):
        """
        test if the business sector fails if it is given an invalid choice
        """
        form = CompanyForm({
            "name": self.name,
            "address": self.address,
            "postcode": self.postcode,
            "registered_company_number": self.registered_company_number,
            "business_sector": "NOT A SECTOR"
            })
        self.assertFalse(
            form.is_valid(),
            "Expecting form with an invalid input for business sector to fail"
            )


class LoanRequestFormTest(TestCase):
    def setUp(self):
        self.amount = 50000
        self.loan_length_days = 40
        self.reason = "Who wouldn't just want some money"
        # Initialise a company object
        self.company = Company.objects.create(
            name="White Glass",
            address="213 Fake Street, Newhaven",
            postcode="UN48 8DF",
            registered_company_number="12345678",
            business_sector=Company.RETAIL
            )

    def test_valid(self):
        form = LoanRequestForm({
            "amount": self.amount,
            "loan_length_days": self.loan_length_days,
            "reason": self.reason
            })
        self.assertTrue(form.is_valid(), "LoanRequestForm submission failed")

    def test_commit(self):
        """Tests successful save to db"""
        form = LoanRequestForm({
            "amount": self.amount,
            "loan_length_days": self.loan_length_days,
            "reason": self.reason
        })
        form.company = self.company
        loanrequest = form.save()
        self.assertEqual(loanrequest.amount, self.amount)
        self.assertEqual(loanrequest.loan_length_days, self.loan_length_days)
        self.assertEqual(loanrequest.reason, self.reason)
        self.assertEqual(loanrequest.company, self.company)

    def test_missing_fields(self):
        form = LoanRequestForm({})
        self.assertFalse(
            form.is_valid(),
            "Form with missing information needs to fail")
        self.assertEqual(
            form.errors,
            {"amount": ["This field is required."],
             "loan_length_days": ["This field is required."],
             "reason": ["This field is required."]},
            "Unexpected response in errors with missing fields"
            )

    def test_amount_too_small(self):
        # A test that should fail if the amount is < 0
        form = LoanRequestForm({
            "amount": -20,
            "loan_length_days": self.loan_length_days,
            "reason": self.reason
        })
        self.assertFalse(
            form.is_valid(),
            "Form should not validate if the loan amount is < 10,000"
        )

    def test_amount_too_large(self):
        # A test that should fail if the amount is < 0
        form = LoanRequestForm({
            "amount": 1000000000.0,
            "loan_length_days": self.loan_length_days,
            "reason": self.reason
        })
        self.assertFalse(
            form.is_valid(),
            "Form should not validate if the loan amount is > 100,000"
        )

