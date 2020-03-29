from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('signup/', views.signup_view, name="signup"),
    path('create/', views.article_create, name="create"),
    url(r'^dashboard/(?P<slug>[\w-]+)/edit/$', views.article_edit, name = 'edit'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_view),
    url(r'^dashboard/(?P<slug>[\w-]+)/$', views.article_view),
]

#in case some one wants to access the static files, CSS, JS, etc..
urlpatterns += staticfiles_urlpatterns()