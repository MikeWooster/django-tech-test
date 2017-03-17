from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User as UserAuth
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

from .forms import UserForm, CompanyForm, LoanRequestForm, PasswordForm
from .models import User


def redirect_to_borrowing(request):
    """redirection to the borrowing page"""
    return redirect("borrowingindex")


def index(request):
    """View to handle the form for collecting information and for parsing it"""
    if request.method == "POST":
        userform = UserForm(request.POST)
        companyform = CompanyForm(request.POST)
        loanrequestform = LoanRequestForm(request.POST)
        passwordform = PasswordForm(request.POST)
        if (userform.is_valid() and companyform.is_valid()
                and loanrequestform.is_valid() and passwordform.is_valid()):
            # Save the companyform first as this is the one without
            # any relationships
            company = companyform.save()
            # Create a username/password from the email/password provided
            passwordentry = passwordform["password"]
            userauth = UserAuth.objects.create(
                username=userform["email"], password=passwordentry
                )
            # Save the userform and loanrequestform after setting the
            # company attribute to associate foreignkeys
            userform.company = company
            userform.userauth = userauth
            user = userform.save()
            loanrequestform.company = company
            loanrequestform.save()
            # Automatically log the user in
            login(request, userauth)
            return redirect("summary", user_id=user.pk)
    else:
        userform = UserForm()
        companyform = CompanyForm()
        loanrequestform = LoanRequestForm()
        passwordform = PasswordForm()

    forms = {"userform": userform,
             "companyform": companyform,
             "loanrequestform": loanrequestform,
             "passwordform": passwordform}
    return render(request, "borrowing/index.html", forms)


def summary(request, user_id):
    """View to provide basic feedback for the latest loan request"""
    user = get_object_or_404(User, pk=user_id)
    if request.user.is_authenticated and user.userauth == request.user:
        company = user.company
        loan = company.loanrequest_set.last()
        return render(
            request,
            "borrowing/summary.html",
            {"forename": user.forename,
             "loan_amount": loan.amount,
             "reason": loan.reason})
    else:
        return HttpResponse(
            "user is not logged in or not allowed to view this page"
        )