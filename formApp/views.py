from django.shortcuts import render, redirect
from formApp.form import ContactForm
from formApp.models import User

def home_view(request):
    return render(request, 'html/home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # form.send_email()
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            
            #save data into database
            #method 1
            # from .models import User
            # User.objects.create(name=name, email=email, message=message)
            
            #method 2
            data = User( name = name, email = email, message = message)
            data.save()
            
            #to update data set the id then do
            
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'html/contact.html', {"form": form})

def contact_success_view(request):
    return render(request, 'html/success.html')