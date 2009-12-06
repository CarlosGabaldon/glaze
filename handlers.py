

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
import markdown

#globals = {'markdown': markdown.markdown}
#render = web.template.render('templates', globals=globals)

render = web.template.render('templates/')

urls = (
    '/index/', 'content_list',
    '/content/(.*)', 'content',
    '/discussions/(.*)', 'discussion_list',
    '/discussion/(.*)', 'discussion'
)
app = web.application(urls, globals())
#app = web.application(urls)

class content_list(object):
    
    def GET(self):
        sql = "select permalink, title from content"
        content_results = data.execute_sql(sql=sql)
        contents = []
        for col in content_results:
            content = {}
            content["permalink"] = col[0]
            content["title"] = col[1]
            contents.append(content)
             
        return render.content_list(contents)
        
        
class content(object):
        
    def GET(self, permalink):
        
        # to-do santize input..
        sql = "select * from content where permalink='%s'" % permalink
        results = data.execute_sql(sql=sql)
        content = {}
        for col in results:
              content["id"] = col[0]
              content["title"] = col[1]
              content["permalink"] = col[2]
              content["body"] = unicode(col[3], 'utf-8')
              content["created"] = col[4].strftime('%Y/%m/%d')
        
        return render.content_view(content, markdown.markdown)
    
    def POST(self, title, path_to_content):
        pass


class discussion_list(object):

    def GET(self, content_id):
        sql = "select id, coordinates from discussion where content_id='%s'" % content_id
        discussion_results = data.execute_sql(sql=sql)
        discussions = []
        for col in discussion_results:
            discussion = {}
            discussion["id"] = col[0]
            discussion["coordinates"] = col[1]
            discussions.append(discussion)
             
        return json.dumps(obj=discussions, sort_keys=True, indent=4)

class discussion(object):

    def GET(self, discussion_id):
        
        sql = "select * from discussion where id='%s'" % discussion_id
        results = data.execute_sql(sql=sql)
        discussion = {}
        for col in results:
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

        return json.dumps(obj=discussion, sort_keys=True, indent=4)
            
    def POST(self, title):
        pass
    

class post(object):
        
    def GET(self, permalink):
        pass
    
    def POST(self, title):
        pass
    
        
        
if __name__ == "__main__":
    app.run()




        
        