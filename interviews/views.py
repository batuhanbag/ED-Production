from django.db import models
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse, HttpResponseRedirect
from .models import Interviews, Comment
import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.


def interviews(request):

    interviews = Interviews.objects.all()

    return render(request, "interviews.html", {"interviews": interviews})


def detail(request, id):

    interviews = get_object_or_404(Interviews, id=id)

    current_detail = interviews

    week_ago = datetime.date.today() - datetime.timedelta(days=30)

    sideInterviews = Interviews.objects.filter(created_date__gte=week_ago).order_by(
        '-read').exclude(title=current_detail)[:3]

    interviews.read += 1

    interviews.save()

    is_liked = False
    is_favourite = False

    if interviews.likes.filter(id=request.user.id):
        is_liked = True

    if interviews.favourite_interviews.filter(id=request.user.id):
        is_favourite = True

    comments = interviews.comments.all()

    context = {
        'interviews': interviews,
        'comments': comments,
        'is_liked': is_liked,
        'is_favourite': is_favourite,
        'total_likes': interviews.total_likes(),
        "sideInterviews": sideInterviews
    }

    return render(request, "interviewsDetail.html", context)


@login_required(login_url="account:login")
def like_post_interviews(request, id):

    post = get_object_or_404(Interviews, id=id)

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

    post = get_object_or_404(Interviews, id=id)

    if post.favourite_interviews.filter(id=request.user.id):
        post.favourite_interviews.remove(request.user)
    else:
        post.favourite_interviews.add(request.user)

    return HttpResponseRedirect(post.get_absolute_url())


@login_required(login_url="account:login")
def addComment(request, id):

    interviews = get_object_or_404(Interviews, id=id)

    if request.method == "POST":
        comment_author = request.user.fullName
        comment_content = request.POST.get("comment_content")
        comment_photo = request.user.account_avatar.url
        newComment = Comment(comment_author=comment_author,
                             comment_content=comment_content,
                             comment_photo=comment_photo)

        newComment.interviews = interviews

        newComment.save()

    return redirect(reverse("interviews:detail", kwargs={"id": id}))
