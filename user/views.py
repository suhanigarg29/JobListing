from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'user/login.html')


@login_required
def account(request):
    context = {
        'account_page': "active",
    }
    return render(request, 'user/account.html', context)


def privacy(request):
    return render(request, 'user/privacy.html')


def terms(request):
    return render(request, 'user/terms.html')


def pricing(request):
    context = {
        'rec_navbar': 1,
    }
    return render(request, 'user/pricing.html', context)