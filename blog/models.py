from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=120)
    post_text = models.TextField()
    author = models.ForeignKey(User)
    date_pub = models.DateTimeField(default=timezone.now)
    likeit = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_pub',)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post_id = models.ForeignKey(Post)
    comment_text = models.TextField()
    date_pub = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User)

    def __str__(self):
        return '{0} {1}'.format(self.post_id, self.author)

    class Meta:
        ordering = ('-date_pub',)


class Like(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s %s' % (self.post_id, self.user)
