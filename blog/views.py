from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post #현재디렉토리(.) models에서 Post를 가져와라
from .forms import PostForm

def post_list(request):
    
    #Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    #데이터준비하기
    qs = Post.objects.all() # Post의 전체 목록을 가져오겠다
    qs = qs.filter(published_date__lte=timezone.now())
    qs = qs.order_by('published_date')

    #데이터넘기기
    return render(request, 'blog/post_list.html', {
        'post_list': qs,   #html에서 호출하는 이름
    }) #render: 장고가지원하는 템플릿해석

def post_detail(request, pk):
    
    # try:
    #     #호출하는 blog번호에 따라 pk값이 들어온다
    #     post = Post.objects.get(pk=pk)   #pk=pk :: (필드명:인자로 받은 pk변수)
    # except Post.DoesNotExitst:
    #     raise Http404 #Page Not Found : from django.http import Http404

    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html',{
        'post' : post,
    })

def post_new(request):
    # 글을 등록하려고 하면 request.POST, request.FILES에 값을 넣는다

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        #request방식이 POST이면 request.POST, request.FILES에서 값을 가져와서 form을 만들어 달라
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html',{
        'form' : form,
    })


def post_edit(request, pk):   
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post) 
        # new랑 동일한데, 수정하고자 하는 글의 post모델 instance를 가져온다
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html',{
        'form' : form,
        
    })