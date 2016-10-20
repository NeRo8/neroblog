"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from blog.views import PostListView, PostDetailView, PostLike, NewComment, PostUpdate, PostDelete, PostCreate
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import DinamicSitemap

sitemaps = {'post': DinamicSitemap}

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post-list'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'^create-post/$', PostCreate.as_view(), name='create-post'),
    url(r'^(?P<pk>\d+)/update-post/$', PostUpdate.as_view(), name='update-post'),
    url(r'^(?P<pk>\d+)/delete-post/$', PostDelete.as_view(), name='delete-post'),

    url(r'^(?P<pk>\d+)/create-comment/$', NewComment, name='create-comment'),
    url(r'^(?P<pk>\d+)/article-like/$', PostLike, name='article-like'),

]
urlpatterns += [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
