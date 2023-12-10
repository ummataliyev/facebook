from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime


from api.models import FacebookPost
from api.scripts.more_pages import more_pages
from api.scripts.single_pages import single_page


class FacebookSinglePostsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        post_url = request.query_params.get('post_url', None)

        if not post_url:
            return Response({'error': 'Missing required parameters!'}, status=status.HTTP_400_BAD_REQUEST)

        data = single_page([post_url])

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


class FacebookMorePostsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        account = request.query_params.get('account')
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        if not account or not start_date_str or not end_date_str:
            return Response({'error': 'Missing required parameters!'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_year, start_month, start_day = map(int, start_date_str.split(','))
            end_year, end_month, end_day = map(int, end_date_str.split(','))

            start_date = datetime(start_year, start_month, start_day)
            end_date = datetime(end_year, end_month, end_day)

        except (ValueError, TypeError):
            return Response({
                'error': 'Invalid date format. Use YYYY, MM, DD.'}, status=status.HTTP_400_BAD_REQUEST)

        data = more_pages(account, start_date, end_date)

        response_data = {
            'status': 'Success',
            'data': data
        }

        return Response(response_data, status=status.HTTP_200_OK)
