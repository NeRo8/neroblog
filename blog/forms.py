from django.forms import ModelForm, Textarea, TextInput
from django.utils.translation import ugettext_lazy

from .models import Comment, Post


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        labels = {
            'comment_text': ugettext_lazy('Comment')
        }
        widgets = {
            'comment_text': Textarea(attrs={'cols': 140, 'rows': 20})
        }


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post_text']
        labels = {
            'title': ugettext_lazy('Title'),
            'post_text': ugettext_lazy('Text'),
        }

        widgets = {
            'post_text': Textarea(attrs={'cols': 140, 'rows': 20}),
            'title': TextInput(attrs={'size': 120})
        }