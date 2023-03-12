
from django import forms
from NewsPaper.news_paper.models import Post

class PstForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = '__all__'

f = PstForm(Post.objects.get(pk =1))

print(f.e)