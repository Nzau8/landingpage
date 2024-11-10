from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    if request.method == "POST":
        # Handle form submission (sending email, saving to database, etc.)
        pass
    return render(request, 'contact.html')