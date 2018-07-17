
"""
from django.core.serializers import json
from django.shortcuts import render

# Create your views here.


def index(request):
	return render(request, 'login.html')


def home(request):
	if request.method == 'POST':
		a = json.loads(request.body)
		print(a)
	return render(request, 'home.html')
"""
"""
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import SuperUser
from django.template import RequestContext


def login(request):  # 登陆页面
	return render(request, 'login.html',)


def loginVerify(request):  # 登陆信息提交验证
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		users = SuperUser.objects.all()
		for user in users:
			if user.username == username and user.password == password:
				user_list = SuperUser.objects.all()
				context = {'user_list': user_list}
			return HttpResponse('1')
			# return render(request, 'home.html', context)
		return HttpResponse('-1')
	else:
		return HttpResponse('0')


def index(request):  # 登陆成功之后跳转的页面
	user_list = SuperUser.objects.all()
	context = {'user_list': user_list}
	return render(request, 'home.html', context)



from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


@login_required(login_url='/login/do_login')
def home(request):
	return render(request, 'home.html', {'username': request.user.username})


def do_login(request):
	if request.method == 'GET':
		return render(request, 'login.html')

	username = request.POST.get('username', '')
	password = request.POST.get('password', '')

	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect(reverse('login:home'))
	else:
		return render(request, 'login.html', {
			'username': username,
			'password': password,
		})
"""


from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


@login_required(login_url='/login/do_login')
def home(request):
	return render(
		request,
		'home.html',
		{'username': request.user.username}
	)


def do_login(request):
	if request.method == 'GET':
		return render(request, 'login.html')

	username = request.POST.get('username', '')
	password = request.POST.get('password', '')

	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect(reverse('login:home'))
	else:
		return render(
			request,
			'home.html',
			{
				'username': username,
				'password': password,
			}
		)
