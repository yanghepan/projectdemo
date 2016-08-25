from django.shortcuts import render,redirect
from block.models import Block
from .models import Article
from .forms import ArticleForm
def article_list(request,block_id):
    block_id=int(block_id)
    block=Block.objects.get(id=block_id)
    articles_objs=Article.objects.filter(block=block,status=0).order_by("-id")
    return render(request,"article_list.html",{"articles":articles_objs,"b":block})

def article_create(request,block_id):
    block_id=int(block_id)
    block=Block.objects.get(id=block_id)
    if request.method=="GET":
        return render(request,"article_create.html",{"b":block})
    else:
        form=ArticleForm(request.POST)
        if(form.is_valid()):
            article=Article(block=block,title=form.cleaned_data["title"],
            content=form.cleand_data["content"],status=0)
            article.save()
            return redirect("/article/list/%s"%block_id)
        else:
            return render(request,"article_create.html",{"b":block,"form":form})
#        title=request.POST["title"].strip()
#        content=request.POST["content"].strip()
#        if(not(title and content)):
#            return render(request,"article_create.html",{"b":block,"error":"标题或者内容不能为空！","title":title,"content":content})
#        if(len(title)>100 or len(content)>1000):
#            return render(request,"article_create.html",{"b":block,"error":"标题或者内容内容过长","title":title,"content":content})
#        article=Article(block=block,title=title,content=content,status=0)
#        article.save()
#        return redirect("/article/list/%s"%block_id)
# Create your views here.
