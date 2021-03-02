from django import forms

from .models import PostModel
# class PostForm(forms.Form):
#    title    = forms.CharField(max_length=50)
#    body     = forms.CharField(
#                widget=forms.Textarea
#    )
#    category = forms.CharField(max_length=50)

class PostForm(forms.ModelForm):
   class Meta:
      model = PostModel
      fields = [
         'author',
         'title',
         'body',
         'category'
      ]