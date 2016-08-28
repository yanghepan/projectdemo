from django.shortcuts import render,redirect
from block.models import Block
from .models import Article
from .forms import ArticleForm
from django.core.paginator import Paginator
def article_list(request,block_id):
    block_id=int(block_id)
    block=Block.objects.get(id=block_id)
    ARTICLE_CNT_1PAGE=1
    page_no=int(request.GET.get("page_no","1"))
#    start_index=(page_no-1)*ARTICLE_CNT_1PAGE
#    end_index=page_no*ARTICLE_CNT_1PAGE
#    articles_objs=Article.objects.filter(block=block,status=0).order_by("-id")[start_index:end_index]
    all_articles=Article.objects.filter(block=block,status=0).order_by("-id")
    p=Paginator(all_articles,ARTICLE_CNT_1PAGE)
    page_links=[i for i in range(page_no-5,page_no+6) if i>0 and i<=p.num_pages]
    page=p.page(page_no)
    page_cnt=p.num_pages,           
    previous_link=page_links[0] - 1
    next_link=page_links[-1] + 1
    pagination_data={"has_previous":previous_link>0,
                     "has_next":next_link<=p.num_pages,
                     "previous_link":previous_link,
                     "next_link":next_link,
                     "page_cnt":p.num_pages,
                     "current_no":page_no,
                     "page_links":page_links} 
    articles_objs=page.object_list
    return render(request,"article_list.html",{"articles":articles_objs,"b":block,"p":pagination_data})

def article_detail(request,article_id):
    article_id=int(article_id)
    article=Article.objects.get(id=article_id)
    return render(request,"article_detail.html",{"article":article})

def article_create(request,block_id):
    block_id=int(block_id)
    block=Block.objects.get(id=block_id)
    if request.method=="GET":
        return render(request,"article_create.html",{"b":block})
    else:
        form=ArticleForm(request.POST)
        if(form.is_valid()):
            article=form.save(commit=False)
            article.block=block
            article.status=0
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
