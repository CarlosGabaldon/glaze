


class Content(object):
    
    @classmethod
    def find_by_permalink(cls, permalink):
        """ Return the content form the content repo by the permalink """
        return None
    
    def _get_discussions(self):
        """ Return the list of discussions for this piece of content """
        return "" # Discussion.objects.filter(Content=self)
    discussions = property(_get_discussions)

