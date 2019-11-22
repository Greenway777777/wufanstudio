# -*- coding: utf-8 -*-

from django.http import HttpResponse,Http404
from django.shortcuts import render
import datetime

def hello(request):
    context          = {}
    now = datetime.datetime.now();
    context['hello'] = '当前北京时间：'+' %s' % now
    return render(request, 'hello.html', context)

def hello2(request,offset):
    context          = {}
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = (datetime.datetime.now() + datetime.timedelta(hours=offset)).strftime('%Y-%m-%d %H:%M:%S')
    #assert False  触发错误页面
    context['hello'] = '%d 小时后，北京时间为：%s' % (offset, dt)
    return render(request, 'hello.html', context)