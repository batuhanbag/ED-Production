from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse, HttpResponseRedirect
from .forms import ArticleForm, ArticleSend
from .models import Article, Comment, sendArticle
import datetime
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
# Create your views here.


def articles(request):
    keyword = request.GET.get("keyword")
    keyword_category = request.GET.get("keyword_category")

    print(keyword_category)

    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "articles.html", {"articles": articles})

    if keyword_category:
        articles = Article.objects.filter(
            article_category__contains=keyword_category)
        return render(request, "articles.html", {"articles": articles})

    articles = Article.objects.all()

    context = {
        "articles": articles,

    }
    return render(request, "articles.html", context)


def index(request):

    keyword = request.GET.get("keyword")

    keyword_category = request.GET.get("keyword_category")

    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "articles.html", {"articles": articles})

    if keyword_category:
        articles = Article.objects.filter(
            article_category__contains=keyword_category)

        return render(request, "articles.html", {"articles": articles})

    week_ago = datetime.date.today() - datetime.timedelta(days=45)
    trends = Article.objects.filter(
        created_date__gte=week_ago).order_by('-read')

    carousel_item1 = Article.objects.filter(
        article_category__contains='Yapay Zeka')[:1]

    carousel_item2 = Article.objects.filter(
        article_category__contains='Yazılım')[:1]

    carousel_item3 = Article.objects.filter(
        article_category__contains='Donanım')[:1]

    carousel_item4 = Article.objects.filter(
        article_category__contains='Kripto Para')[:1]

    articles = Article.objects.all()

    context = {
        'trends': trends[:5],
        'articles': articles,
        'carousel_item1': carousel_item1,
        'carousel_item2': carousel_item2,
        'carousel_item3': carousel_item3,
        'carousel_item4': carousel_item4,

    }

    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def detail(request, id):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "articles.html", {"articles": articles})

    article = get_object_or_404(Article, id=id)

    current_detail = article

    url = "http://localhost:8000" + article.get_absolute_url()

    print(url)

    week_ago = datetime.date.today() - datetime.timedelta(days=45)

    sideArticle = Article.objects.filter(created_date__gte=week_ago).order_by(
        '-read').exclude(title=current_detail)[:3]

    article = get_object_or_404(Article, id=id)

    article.read += 1

    article.save()

    is_liked = False
    is_favourite = False

    if article.likes.filter(id=request.user.id):
        is_liked = True

    if article.favourite.filter(id=request.user.id):
        is_favourite = True

    comments = article.comments.all()

    context = {
        'article': article,
        'comments': comments,
        'is_liked': is_liked,
        'total_likes': article.total_likes(),
        'is_favourite': is_favourite,
        'sideArticle': sideArticle,
        'url': url

    }
    return render(request, "detail.html", context)


@login_required(login_url="account:login")
def addComment(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        comment_author = request.user.fullName
        comment_content = request.POST.get("comment_content")
        comment_photo = request.user.account_avatar

        newComment = Comment(comment_author=comment_author,
                             comment_content=comment_content,
                             comment_photo=comment_photo)

        newComment.article = article

        newComment.save()
    return redirect(reverse("article:detail", kwargs={"id": id}))


@login_required(login_url="account:login")
def like_post_article(request, id):

    post = get_object_or_404(Article, id=id)

    is_liked = False

    if post.likes.filter(id=request.user.id):
        post.likes.remove(request.user)
        is_liked = False

    else:
        post.likes.add(request.user)
        is_liked = True

    return HttpResponseRedirect(post.get_absolute_url())


@login_required(login_url="account:login")
def favourite_post(request, id):

    post = get_object_or_404(Article, id=id)

    if post.favourite.filter(id=request.user.id):
        post.favourite.remove(request.user)
    else:
        post.favourite.add(request.user)

    return HttpResponseRedirect(post.get_absolute_url())


def favourite_list(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "articles.html", {"articles": articles})
    user = request.user

    favourite_posts = user.favourite.all()

    context = {
        'favourite_posts': favourite_posts
    }

    return render(request, "favourites.html", context)


def sendArticle(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "articles.html", {"articles": articles})

    name = request.POST.get('name', '')
    post_type = request.POST.get('accType', '')
    subject = name + \
        " İsimli Kullanıcının Gönderisi, Gönderi Tipi : " + post_type
    message = request.POST.get('message', '')

    basemail = 'batuhannbagg@gmail.com'

    sendmail = EmailMessage(

        subject,
        message,
        settings.EMAIL_HOST_USER,
        [basemail]

    )
    if request.method == "GET":
        return render(request, "sendArticle.html")
    else:
        file = request.FILES['file']

    if request.user.is_authenticated == True:

        sendmail.attach(file.name, file.read(), file.content_type)
        print(file, subject, message, post_type)
        sendmail.send()
        return render(request, "sendArticle_OK.html")
    else:
        messages.info(
            request, 'Lütfen işlemi gerçekleştirmek için giriş yapınız.')
        return render(request, "sendArticle.html")


def handler404(request):
    return render(request, '404page.html', status=404)


def handler500(request):
    return render(request, '404page.html', status=500)
