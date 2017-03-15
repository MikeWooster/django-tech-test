from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserForm, CompanyForm, LoanRequestForm

# Create your views here.
def index(request):

    userform = UserForm()
    companyform = CompanyForm()
    loanrequestform = LoanRequestForm()
    if request.method == "POST":
        userform = UserForm(request.POST)
        companyform = CompanyForm(request.POST)
        loanrequestform = LoanRequestForm(request.POST)
        if (userform.is_valid() and companyform.is_valid()
                and loanrequestform.is_valid()):
            # Process the form data here and commit to db
            pass

    forms = {"userform": userform,
             "companyform": companyform,
             "loanrequestform": loanrequestform}
    return render(request, "borrowing/index.html", forms)