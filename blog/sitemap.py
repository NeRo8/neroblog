from django.contrib.sitemaps import Sitemap
from .models import Post
from django.core.urlresolvers import reverse


class DinamicSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, post):
        return post.date_pub

    def location(self, post):
        return reverse('post-list')
