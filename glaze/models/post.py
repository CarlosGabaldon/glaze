


class Post(object):
    
    # The user the made the post.
    posted_by = models.ForeignKey(User, related_name='posted_by_id')
    
    # The dicussion that this post is a part of.
    discussion = models.ForeignKey(Discussion)
    
    # The text of the post.
    text = models.CharField(maxlength=5000)
    
    # The date posted.
    date = models.DateTimeField(editable=False)
    
    # The post that is post is replying to.
    reply_to = models.IntegerField(blank=True, null=True)
    


