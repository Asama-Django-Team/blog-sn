from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
        "Personal":[
        {
        "first_name":"ali",
        "last_name":"hejazi",
        },
        {
        "first_name":"ali",
        "last_name":"hejazi",
        },
                            ]
    }

    return render(request, 'blog/home.html',context)