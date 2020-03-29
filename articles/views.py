from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Article
from . import forms

def homepage(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('dashboard')

	else:
		form = AuthenticationForm()

	art = Article.objects.all()
	#For login status
	logged_in = 'Negative'
	if request.user.is_authenticated:
		logged_in = 'Positive'

	return render(request, 'homepage.html', {'form' : form, 'articles': art, 'logged_or_not': logged_in})

@login_required(login_url = 'homepage')
def dashboard(request):

	articles = Article.objects.all()
	articlezz = [i for i in articles if i.author == request.user]
	
	return render(request, 'dashboard.html', {'yo_articles': articlezz})

def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		#is password valid? does user exist? all that stuff
		if form.is_valid():
			user = form.save()
			#Log him in automatically
			login(request, user)
			return redirect('homepage')

	else:
		form = UserCreationForm()
	return render(request, 'signup.html' , {'form': form})

#To view articles
def article_view(request,  slug):
	article = Article.objects.get(slug = slug)
	return render(request, 'viewArticle.html', {'article': article})

@login_required(login_url = 'homepage')
def article_create(request):
	if request.method == 'POST':
		form = forms.CreateArticle(request.POST)
		temp = form.save(commit = False)
		temp.author = request.user
		#to make slug
		s = ''
		for i in str(temp.title).lower():
			if i in 'abcdefghijklmnopqrstuvwxyz ':
				s += i
		temp.slug = '-'.join(s.split())
		temp.save()

		return redirect('dashboard')
	else:
		form = forms.CreateArticle()

	return render(request, 'articleCreate.html', {'form': form})

@login_required(login_url = 'homepage')
def article_edit(request, slug):
	article = Article.objects.get(slug = slug)
	if request.method == 'POST':
		form = forms.CreateArticle(request.POST, instance = article)
		form.save()
		return redirect('dashboard')
	else:
		form = forms.CreateArticle(instance = article)
	return render(request, 'editArticle.html', {'form': form, 'slug':slug})