from django.shortcuts import render,redirect
from django.contrib.auth.models import User
def register(request):
    if request.method=="GET":
        return render(request,"register.html")
    else:
        form=RegisterForm(request.POST)
        if(form.is_valid()):
            user=User.objects.create_user(form.username,form.password,form.email)
            user.is_active=True
            user.save()
            return redirect("templates/index.html")
# Create your views here.

