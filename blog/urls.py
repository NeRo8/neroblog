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
from . import views
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import DinamicSitemap

sitemaps = {'post': DinamicSitemap}

# post
urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post-list'),
    url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post-detail'),
    url(r'^create-post/$', views.PostCreate.as_view(), name='create-post'),
    url(r'^(?P<pk>\d+)/update-post/$', views.PostUpdate.as_view(), name='update-post'),
    url(r'^(?P<pk>\d+)/delete-post/$', views.PostDelete.as_view(), name='delete-post'),
    url(r'^(?P<pk>\d+)/article-like/$', views.PostLike, name='article-like'),
]
# comment
urlpatterns += [
    url(r'^(?P<pk>\d+)/create-comment/$', views.CommentCreate.as_view(), name='create-comment'),
    url(r'^(?P<post_id>\d+)/(?P<pk>\d+)/update-comment/$', views.CommentUpdate.as_view(), name='update-comment'),
    url(r'^(?P<post_id>\d+)/(?P<pk>\d+)/delete-comment/$', views.CommentDelete.as_view(), name='delete-comment'),
]

urlpatterns += [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
