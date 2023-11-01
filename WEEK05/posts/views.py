from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.generic import ListView
from .models import Post

# Create your views here.

def index(request):
    return render(request, 'index.html')

def post_diary_view(request):
    return render(request, 'posts/post_diary.html')

def post_song_view(request):
    return render(request, 'posts/post_song.html')

def post_photo_view(request, id):
    return render(request, 'posts/post_photo.html')

def post_sns_view(request, id):
    return render(request, 'posts/post_sns.html')
#CBV
class class_view(ListView):
    model = Post
    template_name='cbv_view.html'

#FBV
def url_view(request):
    data ={'code': '001', 'msg':'OK'}
    return HttpResponse('<h1>url_views</h1>')

def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f'username: {username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')
    print(f'request.GET: {request.GET}')
    print(f'request.POST: {request.POST}')
    return render(request, 'view.html')