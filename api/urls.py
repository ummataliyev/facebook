from django.urls import path

from api.views import FacebookMorePostsAPIView
from api.views import FacebookSinglePostsAPIView

urlpatterns = [
    path('single_pages/', FacebookSinglePostsAPIView.as_view(), name='single'),
    path('more_pages/', FacebookMorePostsAPIView.as_view(), name='extra')
]
