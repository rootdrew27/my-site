from django.shortcuts import render
from Blog.models import Post, Comment
from Blog.forms import CommentForm

# Create your views here.
def BlogIndex(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts
    }
    return render(request, 'blog_index.html', context)


def BlogDetail(request, pk:int):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post) 
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return(request, 'blog_detail.html', context)

def BlogCategory(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        'category': category,
        'posts': posts
    }
    return(request, 'blog_category.html', context)