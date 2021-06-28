from article.models import Article
from django.db import models
from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse, HttpResponseRedirect
from .models import Journals
from django.contrib.auth.decorators import login_required


def journals(request):

    journals = Journals.objects.all()

    return render(request, "journals.html", {"journals": journals})
