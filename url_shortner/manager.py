"""Manager for URLBase model."""
from .models import URLBase
import random 
import string

class URLManager:
    """Url Manager."""

    def create(self,url):
        """Create a url object."""
        slug = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        url_obj = URLBase.objects.create(url=url,short_url=slug)
        return url_obj
    
    def delete(self,slug):
        """delete a url object."""
        try:
            url_obj = URLBase.objects.get(short_url = slug)
            deleted = url_obj.delete()
            return deleted
        except URLBase.DoesNotExist:
            return None
    
    def modify(self,long_url,short_url):
        """modify the long url."""
        try:
            url = URLBase.objects.get(short_url=short_url)
            url.url = long_url
            url.save()
            return url
        except URLBase.DoesNotExist:
            return None
        
    def retrieve_all(self):
        """Retrives all the urls."""
        urls = URLBase.objects.all()
        return urls
    
    def retrieve(self,short_url):
        """Retrieve a single object matching short_url."""
        try:
            url = URLBase.objects.get(short_url=short_url)
            return url
        except URLBase.DoesNotExist:
            return None