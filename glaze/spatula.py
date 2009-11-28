
#######################################################################################
# SHOULD THIS BE API BE A RESTFUL WEB SERVICE INTERFACE THAT RETURNS JSON OR XML DATA???
# THEN APPLICATIONS COULD BE BUILD AGAINST THIS API 
#######################################################################################

# JavaScript ajax application <----JSON----> glaze Restful web service api

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
# <content>
#   <title/>
#   <permalink/>
#   <discussions>
#       <discussion>
#           <title/>
#           <permalink/>
#           <posts>
#              <post>
#                 <title/>
#                 <permalink/>
#              </post>
#           </posts>
#       </dicsusion>
#   </discusions>
# </content>


class Spatula(object):
    """
    A Spatula is the object (tool) used to manage the content and discussions
    annotated on that content.
    
    All model objects have a permalink, which is created when the object is created.

    Examples::

        >>> import glaze
        >>> import glaze.models
        >>> spatula = Spatula()
        >>> content_list = spatula.list_content()

        >>> content = spatula.get_content(permalink="2004-06-30-World-Class-Supply-Management")
        >>> for discussion in content.discussions:
        >>>     print(discussion.coordinates)
        
        
    """
    
    # CONTENT #1
    # permalink = <date>-<title>
    # 2004-06-30-World-Class-Supply-Management
    def new_content(self, title, path_to_content):
        pass
        
    def list_content(self, filters):
        pass
        
    def get_content(self, permalink):
        return content.Content.get(permalink=permalink)
    
    def delete_content(self, permalink):
        pass
        
    # DISCUSSION #2
    # permalink = <content-permalink>-<date>-<title>
    # 2004-06-30-World-Class-Supply-Management-2009-11-22-Transformation-in-Relationships
    def new_discussion(self, content, title, coordinates):
        pass
    
    def list_discussions(self, filters):
        pass
    
    def get_discussion(self, permalink):
        pass
        
    def delete_discussion(self, permalink):
        pass
        
    # POST #3 
    # permalink <content-permalink>-<discussion-permalink>-<date>-<title>
    # 2004-06-30-World-Class-Supply-Management-2009-11-22-Transformation-in-Relationships-2009-11-30-Not-Sure-About-This
    def new_post(self, discussion, title):
        pass
    
    def list_posts(self, filters):
        pass
        
    def get_post(self, permalink):
        pass
        
    def delete_post(self, permalink):
        pass
        
        
        
        
        