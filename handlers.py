

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
        for row in results:
              content["id"] = row[0]
              content["permalink"] = row[1]
              content["created "] = row[2].strftime('%Y/%m/%d')
    
        return json.dumps(obj=content, sort_keys=True, indent=4)
    
    def POST(self, title, path_to_content):
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




        
        