from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import FacebookPost
from api.scripts.facebook import fb_posts


class FacebookPostsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        post_url = request.query_params.get('post_url', None)

        if not post_url:
            return Response({'error': 'Missing required parameters!'}, status=status.HTTP_400_BAD_REQUEST)

        data = fb_posts([post_url])

        # Save extracted data in the DB
        for item in data:
            FacebookPost.objects.create(
                post_id=item['post_id'],
                post_link=item['post_link'],
                publish_time=item['published_time'],
                content=item['content'],
                likes=item['likes'],
                reaction_count=item['reaction_count'],
                reaction_type=item['reactions'],
                comment_count=item['comment_count'],
            )

        response_data = {'status': 'success', 'message': 'Data saved successfully', 'data': data}
        return Response(response_data, status=status.HTTP_200_OK)
