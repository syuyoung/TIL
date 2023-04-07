from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField()
    category = forms.ChoiceField(choices=[('개발', '개발'), ('CS', 'CS'),('신기술', '신기술')],
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 200px;'}))
    


    class Meta:
        model = Post
        fields = '__all__'
    
    content = forms.CharField(widget=forms.Textarea)