from django.urls import path
from django.urls import re_path
from.import views

app_name = 'articles'

urlpatterns = [
    path(r'',views.article_list, name="list"),
    path(r'create/',views.create_post,name="createpost"),
    re_path(r'^(?P<slug>[\w-]+)/$',views.article_detail,name="detail")
]
