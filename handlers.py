

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
import web
import MySQLdb
import data


urls = (
    '/content/(.*)', 'content'
)
app = web.application(urls, globals())


class content(object):
        
    def INDEX(self, filters):
        pass
        
    def GET(self, permalink):
        
        sql = "select * from content where permalink='%s'" % permalink
        results = data.execute_sql(sql=sql)
        content = {}
        for col in results:
              content["id"] = col[0]
              content["title"] = col[1]
              content["permalink"] = col[2]
              content["created"] = col[3].strftime('%Y/%m/%d')
        
        sql = "select * from discussion where content_id ='%s'" % content["id"]
        
        results = data.execute_sql(sql=sql)
        discussions = []
        for col in results:
            discussion = {}
            discussion["id"] = col[0]
            discussion["content_id"] = col[1]
            discussion["title"] = col[2]
            discussion["coordinates"] = col[3]
            discussion["created"] = col[4].strftime('%Y/%m/%d')
            discussions.append(discussion)
            
        content["discussions"] = discussions
        
        return json.dumps(obj=content, sort_keys=True, indent=4)
    
    def POST(self, title, path_to_content):
        pass
        
    def PUT(self, permalink):
        pass
    
    def DELETE(self, permalink):
        pass

class discussion(object):

    def INDEX(self, filters):
        pass
        
    def GET(self, permalink):
        pass
    
    def POST(self, title, path_to_content):
        pass
    
    def PUT(self, permalink):
        pass
        
    def DELETE(self, permalink):
        pass
        
class post(object):
 
    def INDEX(self, filters):
        pass
        
    def GET(self, permalink):
        pass
    
    def POST(self, title, path_to_content):
        pass
    
    def PUT(self, permalink):
        pass
        
    def DELETE(self, permalink):
        pass

        
        
if __name__ == "__main__":
    app.run()




        
        