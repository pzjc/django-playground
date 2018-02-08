# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
# Create your views here.
def home(request):
    return HttpResponse("Hello world, Django!")

def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    string = ("title=%s, category=%s, date_time=%s, content=%s"
            %(post.title, post.category, post.date_time, post.content))
    return HttpResponse(string)
    
def test(request):
    return render(request, 'test.html', {'current_time':datetime.now()})
