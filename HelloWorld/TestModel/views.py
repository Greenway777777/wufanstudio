from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'root' and pwd == "123123":
            # 生成随机字符串
            # 写到用户浏览器cookie
            # 保存在服务端session中
            # 在随机字符串对应的字典中设置相关内容
            request.session['username'] = user
            request.session['islogin'] = True
            if request.POST.get('rmb', None) == '1':
                # 认为设置超时时间
                request.session.set_expiry(10)
            return redirect('/index/')
        else:
            return render(request, 'login.html')


def index(request):
    # 获取当前随机字符串
    # 根据随机字符串获取对应的信息
    if request.session.get('islogin', None):
        return render(request, 'index.html', {'username': request.session['username']})
    else:
        return HttpResponse('please login ')


def logout(request):
    del request.session['username']
    request.session.clear()
    return redirect('/login/')

