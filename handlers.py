

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

render = web.template.render('templates/')

urls = (
    '/index/', 'index',
    '/content/(.*)', 'content'
)
app = web.application(urls, globals())


class index(object):
    
    def GET(self):
        name = 'Carlos'    
        return render.index(name)

class content(object):
        
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
            sql_posts = "select * from post where discussion_id ='%s'" % discussion["id"]
            posts_results = data.execute_sql(sql_posts)
            posts = []
            for post_col in posts_results:
                post = {}
                post["id"] = post_col[0]
                post["discussion_id"] = post_col[1]
                post["posted_by_user_id"] = post_col[2]
                post["reply_to_post_id"] = post_col[3]
                post["text"] = post_col[4]
                post["created"] = post_col[5].strftime('%Y/%m/%d')
                posts.append(post)
            discussion["posts"] = posts
            discussions.append(discussion)
        content["discussions"] = discussions
        
        return json.dumps(obj=content, sort_keys=True, indent=4)
    
    def POST(self, title, path_to_content):
        pass
        
class discussion(object):

    def GET(self, permalink):
        pass
    
    def POST(self, title, path_to_content):
        pass
    

class post(object):
        
    def GET(self, permalink):
        pass
    
    def POST(self, title, path_to_content):
        pass
    
        
        
if __name__ == "__main__":
    app.run()




        
        