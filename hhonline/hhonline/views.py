from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm

def home_page(request):
    context = {
    "title":"home_page",
    "content":" welcome to the home page",
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
    "title":"about_page",
    "content":"welcome to the about page",
    }
    return render(request, "home_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
    "title":"contact_page",
    "content":"welcome to the contact page",
    "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get("fullname"))
    #     print(request.POST.get("email"))
    #     print(request.POST.get("content"))
    return render(request, "contact/views.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print("User logged in")
    print(request.user.is_authenticated)
    '''
    "object is not callable" error occurs when you are trying to behave an object like 
    it is a method or function.

    in this case:
    current_user.is_authenticated()

    you are behaveing current_user.is_authenticated as a method but its not a method .
    you have to use it in this way :

    current_user.is_authenticated

    you use "( )" after methods or functions, not objects.
    '''
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user =  authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            # Redirect to a sucess page
            context['form'] = LoginForm()
            return redirect("/login")
        else:
            # Return an 'invalid login' error message.
            print("Error")
    
    return render(request, "auth/login.html", context)


def register_page(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
            print(form.cleaned_data)
    return render(request, "auth/register.html", {})

#def home_page(request):
#    return HttpResponse("Hello World")
