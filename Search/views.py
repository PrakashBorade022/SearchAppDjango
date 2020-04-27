from django.shortcuts import render
from .models import Post

def search(request):
    post = Post.objects.all()
    query = request.GET.get('search')
    if query:

        find_post = post.filter(title__icontains=query)
        return render(request,'resultPage.html',{'result':find_post})
    return render(request,"search.html")

def dynamicPage(request,id):
    obj = Post.objects.get(id=id)
    return render(request,'post1.html',{'obj':obj })
# def post(req):
#     return render(req,'post1.html')
def dynamic(request):
    obj = Post.objects.all()
    return render(request,'post1.html',{'obj':obj })