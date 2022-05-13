from django.shortcuts import render


def index(request):
    """
    A view to return the index page
    """
    return render(request, "home/index.html")

def returns(request):
    """
    A view to return the returns page
    """
    return render(request, "home/returns.html")


def terms(request):
    """
    A view to return the terms and conditions page
    """
    return render(request, "home/terms_and_conditions.html")


def privacy(request):
    """
    A view to return the privacy page
    """
    return render(request, "home/privacy_policy.html")
