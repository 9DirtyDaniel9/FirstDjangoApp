from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm


# создание поста
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'MainPage/post_edit.html', {'form': form})

# Страница со списком постов
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'MainPage/post_list.html', {'posts': posts})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'MainPage/post_edit.html', {'form': form})


# Редактирование поста

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'MainPage/post_detail.html', {'post': post})

# удаление поста


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('edit-page')
    return render(request, 'MainPage/post_delete.html', {'post': post})
















