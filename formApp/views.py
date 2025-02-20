from django.shortcuts import render, redirect
from formApp.form import ContactForm
# Create your views here.

# def index(request):
#     return HttpResponse( "hello world")

def home_view(request):
    return render(request, 'html/home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            # name = form.cleaned_data["name"]
            # email = form.cleaned_data["email"]
            # message = form.cleaned_data["message"]
            # print(f"Message is sent from {name} ({email}): {message}")
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'html/contact.html', {"form": form})

def contact_success_view(request):
    return render(request, 'html/success.html')