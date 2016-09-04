from django.db import models
from django.contrib.auth.models import User
class ActivateCode(models.Model):
    owner=models.ForeignKey(User,verbose_name="用户")
    code=models.CharField("激活码",max_length=100)
    expire_timestamp=models.DateTimeField()

    create_timestamp=models.DateTimeField("创建时间",auto_now_add=True)
    last_update_timestamp=models.DateTimeField("最后更新时间",auto_now=True)

# Create your models here.
