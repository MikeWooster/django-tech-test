from django.db import models
from django.contrib.auth.models import User as UserAuth
from django.core.validators import (MinValueValidator,
                                    MaxValueValidator,
                                    MinLengthValidator
                                    )

class Company(models.Model):
    """
    Definition of the company table
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
    name = models.CharField(max_length=64)
    address = models.TextField()
    postcode = models.CharField(max_length=8)
    # The company registration number (CRN) is a unique combination of
    # numbers and in some case letters.  A CharField is a better choice
    # here over an IntegerField
    registered_company_number = models.CharField(
        max_length=8,
        validators=[MinLengthValidator(8)]
        )
    business_sector = models.CharField(
        max_length=2,
        choices=BUSINESS_SECTOR_CHOICES,
        default=RETAIL
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "companies"


class User(models.Model):
    """
    Definition of the user table

    A relationship has been set up to relate this User to a single Customer
    """
    forename = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    email = models.EmailField()
    telephone_number = models.CharField(max_length=15)
    company = models.ForeignKey(Company)
    userauth = models.ForeignKey(UserAuth)

    def __str__(self):
        return "{0}, {1}".format(self.surname, self.forename)

class LoanRequest(models.Model):
    """
    Definition of the loanrequest table

    A relationship has been set up to relate this loan to a single Company.
    """
    company = models.ForeignKey(Company)
    amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(10000.0), MaxValueValidator(100000.0)]
        )
    loan_length_days = models.PositiveSmallIntegerField()
    reason = models.TextField()

    def __str__(self):
        return "borrowing: {0}".format(self.amount)


