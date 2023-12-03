from django.urls import path

from api.views import FacebookPostsAPIView

urlpatterns = [
    path('fb_post/', FacebookPostsAPIView.as_view(), name='get_fb_content')
]
