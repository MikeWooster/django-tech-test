from django.test import TestCase, Client
from ..models import Company
from ..forms import UserForm


class UserFormTest(TestCase):

    def setUp(self):
        self.company = Company.objects.create(
            name="Green Glass",
            address="123 Fake Street, Avenue 1, Borough Green",
            postcode="TN16 8EH",
            registered_company_number="12345678",
            business_sector=Company.RETAIL,
            )
        # Define attributes for consistant usage across tests
        self.forename = "Mike"
        self.surname = "Wooster"
        self.email = "Mike.Wooster@example.com"
        self.tel_no = "+441732777666"

    def test_valid_form(self):
        """Test if a submission of correct data works"""
        form = UserForm({
            "forename": self.forename,
            "surname": self.surname,
            "email": self.email,
            "telephone_number": self.tel_no,
            })
        self.assertTrue(form.is_valid(), "Form submission unsuccessful")

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
