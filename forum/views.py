from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .utils import update_views
from .forms import PostForm, CategoryForm, CommentForm, ReplyForm
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.contrib import messages


def home(request):
    categories = Category.objects.all()
    num_users = Account.objects.all().count()
    num_categories = categories.count()
    num_posts = Post.objects.all().count()
    try:
        last_post = Post.objects.latest("date")
    except:
        last_post = []

    context = {
        "categories": categories,
        "num_users": num_users,
        "num_posts": num_posts,
        "num_categories": num_categories,
        "last_post": last_post,
        "title": "OZONE forum app"
    }
    return render(request, "forum/forums.html", context)


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post).all()
    context = {
        "comments": comments,
        "post": post,
        "title": "OZONE: " + post.title,
    }
    if request.user.is_authenticated:
        if request.method == "POST":
            if 'delete-comment' in request.POST:
                Comment.objects.filter(id=request.POST['delete-comment']).delete()
                messages.success(request, f'Your comment has been deleted')
                return redirect("forum:detail", slug=slug)
            if 'delete-reply' in request.POST:
                Reply.objects.filter(id=request.POST['delete-reply']).delete()
                messages.success(request, f'Your reply has been deleted')
                return redirect("forum:detail", slug=slug)
            if 'delete-post' in request.POST:
                category_slug = Post.objects.filter(slug=request.POST['delete-post']).values('categories__slug')[0]['categories__slug']
                Post.objects.filter(slug=request.POST['delete-post']).delete()
                messages.success(request, f'Your post has been deleted')
                if Post.objects.filter(categories__slug=category_slug).count() == 0:
                    Category.objects.filter(slug=category_slug).delete()
                    return redirect('forum:home')
                return redirect("forum:posts", slug=category_slug)
            comment_form = CommentForm(request.POST, prefix='comment')
            reply_form = ReplyForm(request.POST, prefix='reply')
            author = Account.objects.get(username=request.user.username)
            if (comment_form.is_valid()) and (comment_form['content'].value() is not None):
                new_comment = comment_form.save(commit=False)
                new_comment.user = author
                new_comment.post = post
                new_comment.save()
                update_credits(request, 0.1)
                messages.success(request, f'Your comment has been posted. You have earned 0.1 credits')
                return redirect("forum:detail", slug=slug)
            if (reply_form.is_valid()) and (reply_form['content'].value() is not None):
                new_reply = reply_form.save(commit=False)
                new_reply.user = author
                new_reply.comment = Comment.objects.get(id=request.POST.get('comment_id'))
                new_reply.save()
                update_credits(request, 0.1)
                messages.success(request, f'Your reply has been posted. You have earned 0.1 credits')
                return redirect("forum:detail", slug=slug)
        else:
            comment_form = CommentForm(prefix='comment')
            reply_form = ReplyForm(prefix='reply')
            context = {
                "comment_form": comment_form,
                "reply_form": reply_form,
                "comments": comments,
                "post": post,
                "title": "OZONE: " + post.title,
            }
            update_views(request, post)
            return render(request, "forum/detail.html", context)

    update_views(request, post)
    return render(request, "forum/detail.html", context)


def posts(request, slug):
    if request.method == 'POST':
        Post.objects.filter(slug=request.POST['delete-post']).delete()
        messages.success(request, f'Your post has been deleted')
        if Post.objects.filter(categories__slug=slug).count() == 0:
            Category.objects.filter(slug=slug).delete()
            return redirect('forum:home')
        return redirect('forum:posts', slug=slug)
    else:
        category = Category.objects.get(slug=slug)
        posts = Post.objects.filter(categories=category.id).all()

        context = {
            "posts": posts,
            "forum": category,
            "title": "Studee: Posts"
        }

        return render(request, "forum/posts.html", context)


@login_required
def create_post(request):
    if request.method == "POST":
        post_form = PostForm(request.POST, prefix='post')
        category_form = CategoryForm(request.POST, prefix='category')
        if (category_form.is_valid()) and (post_form['categories'].value() == ''):
            category = category_form.save()
        if post_form.is_valid():
            author = Account.objects.get(username=request.user.username)
            new_post = post_form.save(commit=False)
            new_post.user = author
            if post_form['categories'].value() == '':
                new_post.categories = Category.objects.get(slug=category.slug)
            new_post.save()
            update_credits(request, 0.25)
            messages.success(request, f'Your post has been created. You have earned 0.25 credits')
            return redirect("forum:home")
    else:
        post_form = PostForm(prefix='post')
        category_form = CategoryForm(prefix='category')
        context = {
            "create_form": post_form,
            "cat_form": category_form,
            "title": "Studee: Create New Post"
        }
        return render(request, "forum/create_post.html", context)


# def latest_posts(request):
#     posts = Post.objects.all().filter(approved=True)[:10]
#     context = {
#         "posts": posts,
#         "title": "Studee: Latest 10 Posts"
#     }
#
#     return render(request, "forum/latest_posts.html", context)


def update_credits(request, credits):
    credit_account = Account.objects.get(username=request.user.username)
    credit_account.forum_credits = F('forum_credits') + credits
    credit_account.save()
