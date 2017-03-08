from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse 
from website.forms import ContactForm, UserSignUpForm, LoginForm , ComplainForm
from .models import User

# Create your views here.
def index(request):
    return render(request, "index.html")

def aboutus(request):
    return render(request, "aboutus.html")

def extra(request):
    return render(request, "extra.html")

def profile(request):
    return render(request, "profile.html")

def login(request):
    form = LoginForm()
    return render(request, "login.html", {'form': form, })

def contactus(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, "contactus.html", {'form': form, })
    elif (request.method == 'POST'):
        form = ContactForm(data=request.POST)
        display_message = None
        if form.is_valid():
            form_name = form.cleaned_data['contact_name']
            form_email = form.cleaned_data['contact_email']
            message = form.cleaned_data['content']
            try:
                send_mail(form_name, form_email, message, ['panchalindra153@gmail.com'])
                display_message = "Email has been sent"
            except BadHeaderError:
                display_message = "Invalid Header in Request."
        else:
            display_message = str(form.errors)
    return HttpResponse(display_message)


def signup(request):
    if request.method == 'GET':
        form = UserSignUpForm()
        return render(request, 'signup.html', {'form': form, })
    elif request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("DOne")
        else:
            return HttpResponse(str(form.errors))
        return render(request, "signup.html", {'form': form, })


#@login_required(login_url="login/")
def message(request):
    return render(request, "profile/message.html")


#@login_required(login_url="login/")
def tendar(request):
    return render(request, "profile/tendar.html")


#@login_required(login_url="login/")
def chat(request):
    return render(request, "profile/chat.html")


#@login_required(login_url="login/")
def complain(request):
    if request.method == 'GET':
        form = ComplainForm()
        return render(request, 'profile/complain.html', {'form': form, })
    elif request.method == 'POST' :
        form = ComplainForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect(".")
        else:
            return HttpResponse(str(form.errors))
        return render(request, 'profile/complain.html', {'form': form, })



#@login_required(login_url="login/")
def suggestion(request):
    return render(request, "profile/suggestion.html")
