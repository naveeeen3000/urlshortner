"""Views for URLBase."""
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .manager import URLManager
from django.core.cache import cache

class URLView(APIView):
    """CRUD Views to operate on URLBase model."""

    def __init__(self):
        """init for URLView."""
        self.url_manager = URLManager()

    def get(self,request):
        """Get method to retrieve and redirect to actual URL."""    
        limit = request.GET.get('limit',20)
        page = request.GET.get('page',1)
        if not cache.get("urls"):
            urls = self.url_manager.retrieve_all() 
            data = list(urls.values())
            cache.set('urls',data,86400)
        else:
            data = cache.get("urls")
        res = data[(page-1)*limit : (page-1)*limit + limit]
        cache.set('urls',data)
        return Response({"urls":res},status=status.HTTP_200_OK)

    def post(self,request):
        """Post Method to create a short url and map to actual URL."""
        request_data = request.data
        if not request_data:
            return Response({"error":"data not found in request."},status=status.HTTP_400_BAD_REQUEST)
        long_url = request_data.get('url',None)
        if long_url:
            url = self.url_manager.create(long_url)
            if url:
                return Response({"short_url":request.build_absolute_uri('/')+(url.short_url)},status=status.HTTP_201_CREATED)
            else:
                return Response({"error":"something went wrong while creating short url"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"error":"url key not found in request"},status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        """Delete method to delete a url entry."""
        slug = request.GET.get('slug',None)
        if not slug:
            return Response({"error":"provide slug in the query params"},status=status.HTTP_400_BAD_REQUEST)
        url_deleted = self.url_manager.delete(slug)
        if url_deleted:
            cache.delete('urls')
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"error":"short url not found."},status=status.HTTP_400_BAD_REQUEST)
        

    def patch(self,request):
        """Modify actual long url."""
        request_data = request.data
        if not request_data:
            return Response({"error":"data not found in request."},status=status.HTTP_400_BAD_REQUEST)
        slug = request_data.get("slug")
        new_long_url = request_data.get("long_url")
        if not slug or not new_long_url:
            return Response({"error":"provide all the fields in request"},status=status.HTTP_400_BAD_REQUEST)
        modified = self.url_manager.modify(new_long_url,slug)
        if modified:
            cache.delete('urls')
            return Response(status=status.HTTP_200_OK)
        return Response({"error":"short url not found."},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_absolute_url(request,slug):
    """redirecting to original url."""
    url = URLManager().retrieve(slug)
    if url:
        long_url = url.url
        return redirect(long_url)
    else:
        return Response({"error":"shorturl not found."},status=status.HTTP_404_NOT_FOUND)
    
        