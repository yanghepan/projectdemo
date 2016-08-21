from django.db import models

class Block(models.Model):
    name=models.CharField("板块名称",max_length=100)
    desc=models.CharField("板块描述",max_length=100)
    manager=models.CharField("板块管理员名称",max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name="板块"
        verbose_name_plural="板块"

 
