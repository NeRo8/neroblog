# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from blog.forms import CommentForm, PostForm
from blog.models import Post, Like, Comment


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/post_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post/post_detail.html'

    def get_object(self, queryset=None):
        obj = super(PostDetailView, self).get_object(queryset)
        if obj.status == 'draft':
            raise Http404('Page does not exist or verified by the moderator.')
        else:
            return obj


@method_decorator(login_required, name='dispatch')
class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post/post_create.html'

    def get_success_url(self):
        return reverse('profile')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post/post_create.html'

    def get_success_url(self):
        return reverse('profile')

    def form_valid(self, form):
        form.instance.status = 'draft'
        form.instance.date_pub = timezone.now()
        return super(PostUpdate, self).form_valid(form)

    def get_object(self, queryset=None):
        obj = super(PostUpdate, self).get_object(queryset)
        if obj.author != self.request.user:
            raise Http404('Page does not exist or you are not authorized for this transaction.')
        return obj


@method_decorator(login_required, name='dispatch')
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('profile')
    template_name = 'blog/post/post_delete.html'

    def get_object(self, queryset=None):
        obj = super(PostDelete, self).get_object(queryset)
        if obj.author != self.request.user:
            raise Http404('Page does not exist or you are not authorized for this transaction.')
        return obj


@login_required
def PostLike(request, pk):
    myarticle = Post.objects.get(pk=pk)  # Берем статью з id = pid
    myuser = request.user  # та користувача з id 1

    if not Like.objects.filter(post_id=pk).filter(user=myuser):
        newLike = Like(post_id=myarticle, user=myuser)
        newLike.save()
        myarticle.likeit += 1
        myarticle.save()

    return HttpResponseRedirect(reverse('post-detail', args=[pk]))


@method_decorator(login_required, name='dispatch')
class CommentCreate(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post/comment_create.html'

    def get_success_url(self):
        return reverse('post-detail', args=[self.kwargs['pk']])

    def form_valid(self, form):
        form.instance.post_id_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super(CommentCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class CommentUpdate(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post/comment_create.html'

    def get_success_url(self):
        return reverse('post-detail', args=[self.kwargs['post_id']])


@method_decorator(login_required, name='dispatch')
class CommentDelete(DeleteView):
    model = Comment
    template_name = 'blog/post/comment_delete.html'

    def get_success_url(self):
        return reverse('post-detail', args=[self.kwargs['post_id']])

    def get_object(self, queryset=None):
        obj = super(CommentDelete, self).get_object(queryset)
        if obj.author != self.request.user:
            raise Http404('Page does not exist or you are not authorized for this transaction.')
        return obj
