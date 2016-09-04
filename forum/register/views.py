from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.http import HttpResponse
import uuid
import datetime
from django.utils import timezone
from .models import ActivateCode
from django.core.mail import send_mail
def register(request):
    if request.method=="GET":
        return render(request,"register.html")
    else:
        error=""
        username=request.POST["username"].strip()
        email=request.POST["email"].strip()
        password=request.POST["password"].strip()
        re_password=request.POST["re_password"].strip()
        if not password or not re_password:
            error="密码不能为空!"
        if password != re_password:
            error="两次密码不一致";
        form=RegisterForm(request.POST)
        if(form.is_valid() and not error ):
           user=User.objects.create_user(username=username,email=email,password=password)
           user.is_active=False
           user.save()

           new_code=str(uuid.uuid4()).replace("-","")
           expire_time=timezone.now()+datetime.timedelta(days=2)
           code_record=ActivateCode(owner=user,code=new_code,expire_timestamp=expire_time)
           code_record.save()
           activate_link="http://%s/activate/%s" % (request.get_host(),new_code)
           activate_email='''点击<a href="%s">这里</a>激活''' % activate_link
           send_mail(subject='[篮球部落论坛]激活邮件',
           message='点击链接激活:%s'%activate_link,
           html_message=activate_email,
           from_email='506706547@qq.com',
           recipient_list=[email],
           fail_silently=False) 
           return HttpResponse("注册成功,激活邮件已经发送到您的邮箱，请点击邮箱中的激活链接完成激活。")
        else:
            return render(request,"register.html",{"form":form,"error":error})
def activate(request,code):
    query=ActivateCode.objects.filter(code=code,expire_timestamp__gte=datetime.datetime.now())
    if query.count()>0:
        code_record=query[0]
        code_record.owner.is_active=True
        code_record.owner.save()
        return HttpResponse("激活成功")
    else:
        return HttpResponse("激活失败")
# Create your views here.

