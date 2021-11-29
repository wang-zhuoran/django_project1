import json

from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import TodoModel, Play


def show(request):
    result = TodoModel.objects.all()#获取对象
    plays = []
    for i in result:
        plays.append({'id' : i.id,
                      'title' : i.title,
                      'content' : i.content})
    plays_json = json.dumps(plays,ensure_ascii=False)
    return HttpResponse(plays_json)#转换为json格式


def index(request):
    if request.method == 'POST':
        new = TodoModel(name=request.POST['name'])
        new.save()
        return redirect('/')
    list = TodoModel.objects.all()
    return render(request, 'index.html', {'list': list})
