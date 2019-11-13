from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post
#models'dan önceki nokta, mevcut dizin veya mevcut uygulama anlamına geliyor.
# Hem views.py hem de models.py aynı dizindedir. Bu şu anlama geliyor:

def post_list(request):
    #ORM yani entity frameworkteki kullanımla benzer
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', {'postsKey': posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'postKey': post})
