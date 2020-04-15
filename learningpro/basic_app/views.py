from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def index(request):
    return render(request,"basic_app/index.html")

def register(request):
    registered=False

    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(request.POST,request.FILES)

        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if "picture" in request.FILES:
                profile.picture=request.FILES["picture"]
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,"basic_app/registration.html",{"user_form":user_form,"profile_form":profile_form,"registered":registered})


def user_login(request):
    if request.method=="POST":

        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("account is bocked")
        else:
            print("someone tried to login & failed")
            print("username:{} and password :{}".format(username,password))
            return HttpResponse("invalid login details")
    else:
        return render(request,"basic_app/login.html",{})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required
def special(request):
    return HttpResponse("you are loggedin welcome!")
