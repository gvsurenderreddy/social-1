from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^post/$', views.PostViewList.as_view()),
    url(r'^post&limit=(?P<limit>\d+)/$', views.PostViewList.as_view()),
    url(r'^post/(?P<id>\d+)$', views.PostViewDetail.as_view()),
    url(r'^comment/$', views.CommentViewList.as_view()),
    url(r'^comment/(?P<id>\d+)/$', views.CommentViewDetail.as_view()),
    url(r'^post/(?P<id>\d+)/comment', views.PostComment.as_view()),
    url(r'^wall/(?P<id>\d+)$', views.UserWallDetail.as_view()),
    url(r'^wall/(?P<id>\d+)&limit=(?P<limit>\d+)$', views.UserWallDetail.as_view()),
    url(r'^wall/(?P<id>\d+)/(?P<action>\w+)/(?P<post_id>\d+)$', views.UserWallPegination.as_view()),
    url(r'^wall/(?P<id>\d+)/(?P<action>\w+)/(?P<post_id>\d+)&limit=(?P<limit>\d+)$', views.UserWallPegination.as_view()),
    url(r'^(?P<action>\w+)/(?P<id>\d+)$', views.PostPagination.as_view()),
    url(r'^(?P<action>\w+)/(?P<id>\d+)&limit=(?P<limit>\d+)$', views.PostPagination.as_view()),
]
