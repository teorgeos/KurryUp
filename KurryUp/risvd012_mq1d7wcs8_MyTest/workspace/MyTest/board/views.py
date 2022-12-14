from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    postList = Post.objects.order_by('-date')
    context = {'postList': postList}
    return render(request, 'board/list.html', context)
def detail(request, postId):
    # 상세보기
    post = Post.objects.get(id=postId)
    context = {'post': post}
    return render(request, 'board/detail.html', context)