from django.conf.urls import url  #urls하면 안됨 여긴 url임
from . import views  #현재디렉토리(.)에서 views를 import

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    #url(r'^post/1/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),  #pk라는 이름으로 post_detail의 인자값을 숫자로 넘길꺼야
    url(r'^post/new/$', views.post_new, name='post_new'), # post/new라는 주소로 들어오게 되면, views의 post_new뷰를 호출하게할것이고, 이 패터의 이름은 post_new이다
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

]