
from django import forms
from .models import  Post,Comment



class PostForm(forms.ModelForm):
    name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    surname = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Surname'}))
    age = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Age'}))
    userphoto = forms.ImageField(widget=forms.FileInput(attrs={'placeholder': 'Choose your profile photo'}))
    place = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Place'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'placeholder': 'Choose your place photo'}))
    text = forms.CharField(max_length=50, widget=forms.Textarea(attrs={'placeholder': 'Discription'}))
    class Meta:
        model = Post
        fields = '__all__'



class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'placeholder': 'Write your comment here...','class':'add_comment_text_area'}))
    post_id = forms.IntegerField(widget=forms.HiddenInput)
    class Meta:
        model = Comment
        fields = ['text']
