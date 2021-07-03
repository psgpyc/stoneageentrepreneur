from django.forms import ModelForm
from .models import SharePost,PostComment


class SharePostForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({

            'class': 'post-form-style',
            'placeholder': 'Ask away.',
            'id': 'content-area',
        })

        self.fields['code'].widget.attrs.update({

            'class': 'post-form-style no-view',
            'placeholder': 'Post your code here',
            'id': 'code-area',
        })

        self.fields['content'].label = ''
        self.fields['code'].label = ''

    class Meta:
        model = SharePost
        fields = ['content', 'code']


class CommentPostForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs.update({
            'class': 'input-des',
            'placeholder': 'Press ENTER to add a comment',
            'id': 'input-des-id',
        })

        self.fields['comment'].label = ''

    class Meta:
        model = PostComment
        fields = ['comment']

