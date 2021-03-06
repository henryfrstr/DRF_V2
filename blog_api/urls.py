from django.urls import path
from .views import PostList, PostDetail, PostListDetailfilter
from .views import PostList
from rest_framework.routers import DefaultRouter

app_name = "blog_api"

# router = DefaultRouter()
# router.register('', PostList, basename='post')
# urlpatterns = router.urls

# urlpatterns = [
#     path("<int:pk>", PostDetail.as_view(), name="detailcreate"),
#     path("", PostList.as_view(), name="listcreate"),
# ]

urlpatterns = [
    path('posts/', PostDetail.as_view(), name='detailcreate'),
    path('search/', PostListDetailfilter.as_view(), name='postsearch'),
    path('', PostList.as_view(), name='listcreate'),
]
