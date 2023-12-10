from django.urls import path

from api.views import FacebookPostsAPIView
from api.views import FacebookSinglePostsAPIView

urlpatterns = [
    path('fb_post/', FacebookSinglePostsAPIView.as_view(), name='get_fb_content'),
    path('fb_posts_more/', FacebookPostsAPIView.as_view(), name='get_fb_more')
]
