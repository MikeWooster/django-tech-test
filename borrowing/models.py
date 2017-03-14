from django.db import models


class User(models.Model):
    """
    Definition of the user table
    """
    forename = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    email = models.EmailField()
    telephone_number = models.CharField(max_length=15)


class Company(models.Model):
    """
    Definition of the company table

    A relationship has been set up to relate this loan to a single user
    """
    # Define the choices for the business sector
    RETAIL = "RE"
    PROFESSIONAL_SERVICES = "PS"
    FOOD_AND_DRINK = "FD"
    ENTERTAINMENT = "EN"
    BUSINESS_SECTOR_CHOICES = (
        (RETAIL, "Retail"),
        (PROFESSIONAL_SERVICES, "Professional Services"),
        (FOOD_AND_DRINK, "Food & Drink"),
        (ENTERTAINMENT, "Entertainment"),
        )
    user = models.ForeignKey(User)
    name = models.CharField(max_length=64)
    address = models.TextField()
    postcode = models.CharField(max_length=8)
    # The company registration number (CRN) is a unique combination of
    # numbers and in some case letters.  A CharField is a better choice
    # here over an IntegerField
    registered_company_number = models.CharField(max_length=8)
    business_sector = models.CharField(
        max_length=2,
        choices=BUSINESS_SECTOR_CHOICES,
        default=RETAIL
        )

class LoanRequest(models.Model):
    """
    Definition of the loanrequest table

    A relationship has been set up to relate this loan to a single Company.
    """
    company = models.ForeignKey(Company)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    loan_length_days = models.PositiveSmallIntegerField()
    reason = models.TextField()



