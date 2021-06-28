from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse, HttpResponseRedirect
from .models import News, Comment
import datetime
from django.contrib.auth.decorators import login_required


def detail(request, id):

    news = get_object_or_404(News, id=id)

    current_detail = news

    week_ago = datetime.date.today() - datetime.timedelta(days=45)

    sideNews = News.objects.filter(created_date__gte=week_ago).order_by(
        '-read').exclude(title=current_detail)[:3]

    news.read += 1

    news.save()

    is_liked = False
    is_favourite = False

    if news.likes.filter(id=request.user.id):
        is_liked = True

    if news.favourite_news.filter(id=request.user.id):
        is_favourite = True

    comments = news.comments.all()

    context = {
        'news': news,
        'comments': comments,
        'is_liked': is_liked,
        'total_likes': news.total_likes(),
        'is_favourite': is_favourite,
        'sideNews': sideNews,

    }
    return render(request, "newsDetail.html", context)


@login_required(login_url="account:login")
def like_post_news(request, id):

    post = get_object_or_404(News, id=request.POST.get('post_id'))

    is_liked = False

    if post.likes.filter(id=request.user.id):
        post.likes.remove(request.user)
        is_liked = False

    else:
        post.likes.add(request.user)
        is_liked = True

    return HttpResponseRedirect(post.get_absolute_url())


login_required(login_url="account:login")


def favourite_post(request, id):

    post = get_object_or_404(News, id=id)

    if post.favourite_news.filter(id=request.user.id):
        post.favourite_news.remove(request.user)
    else:
        post.favourite_news.add(request.user)

    return HttpResponseRedirect(post.get_absolute_url())


@login_required(login_url="account:login")
def addComment(request, id):
    news = get_object_or_404(News, id=id)

    if request.method == "POST":
        comment_author = request.user.fullName
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author=comment_author,
                             comment_content=comment_content)

        newComment.news = news

        newComment.save()
    return redirect(reverse("news:detail", kwargs={"id": id}))


def news(request):

    news = News.objects.all()
    return render(request, "news.html", {"news": news})


def about(request):
    return render(request, "about.html")
