from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post  #post에 대한 모델이고
        fields  = ['title', 'text']     #title, text에 대한 입력을 받겠다 리스트로 정의 [], 튜플로도 가능('title', 'text',)
