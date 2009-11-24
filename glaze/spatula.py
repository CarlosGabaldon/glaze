


# 1. Load the Content requested by permalink.
# 2. From the Content load all Discussions.
# 3. From each Discussion load all Posts.
#
# content = Content.find_by_permalink("2004-06-30-World-Class-Supply-Management")
#  # Load the content in the content viewer..
# ..
#  # Annotate the discussions on the content by the discussion.coordinates
# for discussion in content.discussions:
#     # mark content with discussion.coordinates
#


class Spatula(object):
    """
    A Spatula is the object (tool) used to manage the content and discussions
    annotated on that content.

    Examples::

        >>> import glaze
        >>> import glaze.models
        >>> spatula = Spatula()
        >>> content_list = spatula.list_content()

        >>> content = spatula.get_content(permalink="2004-06-30-World-Class-Supply-Management")
        >>> for discussion in content.discussions:
        >>>     print(discussion.coordinates)
        
        
    """
    def __init__(self, name):
        """
        Initialize a newly instanced Spatula

        `name`
            is the name of the spatula

        """
        self.name = name
        
    def list_content(self):
        pass
        
    def get_content(self, permalink):
        pass
        
    def add_content(self, content):
        pass
    
    def remove_content(self, permalink):
        pass