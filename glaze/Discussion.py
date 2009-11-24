

class Discussion(object):
    
    # Relates this discussion to a piece of content.
    content_id = models.ForeignKey(Content)
    
    # Specifies where within the content the dicussion is happening.
    coordinates = models.CharField(maxlength=500)  
    
    # The list of the posts within this discussion..
    def _get_posts(self):
        """Return list of the posts within this discussion. """
        return "" # Post.objects.filter(discussion=self)
    posts = property(_get_posts)
