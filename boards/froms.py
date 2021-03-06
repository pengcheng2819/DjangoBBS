# 作者      : pengcheng
# 创建时间  : 2020/6/5 12:00 

from django import forms
from .models import Topic
from .models import Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':5,'placeholder':'what is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000!')

    class Meta:
        model = Topic
        fields = ['subject','message']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message']