from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Article
# Create your views here.
# def home(request):
#     return HttpResponse('hiiiiiii')

# def api(request):
#     data = {
#         "name": "ali",
#         "last_name": "hejazi",
#         "job":
#     }
#     return JsonResponse()

def home(request):
    context = {
        "articles": Article.objects.all()
    }

    return render(request, 'blog/home.html',context)


def detail(request, slug):
    context = {
        "article": Article.objects.get(slug=slug)
    }

    return render(request, 'blog/detail.html',context)