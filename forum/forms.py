from django import forms
from .models import Post, Category, Comment, Reply


class PostForm(forms.ModelForm):
    categories = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Post
        fields = ["title", "content", "categories", "tags"]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    title = forms.CharField(required=False)
    description = forms.CharField(required=False)

    class Meta:
        model = Category
        fields = ["title", "description"]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Enter your comment here', 'style': 'height:4rem!important'}))

    class Meta:
        model = Comment
        fields = ["content"]


class ReplyForm(forms.ModelForm):
    content = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Enter your reply here', 'style': 'height:4rem!important'}))

    class Meta:
        model = Reply
        fields = ["content"]
