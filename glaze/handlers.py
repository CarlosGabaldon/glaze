

# JavaScript ajax application <----JSON----> Python glaze Restful web service api

#{
#     "title": "World Class Supply Management",
#     "permalink": "2004-06-30-World-Class-Supply-Management",
#     "discussions": 
#     [
#        { 
#            "title": "Transformation in Relationships", 
#            "permalink": "2004-06-30-World-Class-Supply-Management-2009-11-22-Transformation-in-Relationships",
#            "posts": 
#            [
#                {
#                "title": "Not Sure About This", 
#                "permalink": "2004-06-30-World-Class-Supply-Management-2009-11-22-Transformation-in-Relationships-2009-11-30-Not-Sure-About-This"
#                }
#            
#           ],
#        },
#        { 
#            "title": "Transactional Relationships", 
#            "permalink": "2004-06-30-World-Class-Supply-Management-2009-10-02-Transactional-Relationships",
#            "posts":
#            [
#            
#            
#            ],
#        },
#     ]
# }



import json
import MySQLdb
import models
import data

class Handler(object):
    """
    A Handler is the main request handler used to serve up the content with the discussions
    annotated on that content.
    

    Examples::

        
    """
    
    # CONTENT #1
    # permalink = <date>-<title>
    # 2004-06-30-World-Class-Supply-Management
    def new_content(self, title, path_to_content):
        pass
        
    def list_content(self, filters):
        pass
        
    def get_content(self, permalink):
        
        sql = "select * from content where permalink='%s'" % permalink
        results = data.execute_sql(sql=sql)
        content = {}
        for row in results:
              content["id"] = row[0]
              content["permalink"] = row[1]
              content["created "] = row[2].strftime('%Y/%m/%d')
        
        return json.dumps(obj=content, sort_keys=True, indent=4)
    
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
        
        
        
        
        