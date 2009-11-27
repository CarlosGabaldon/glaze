import MySQLdb
import data



class Content(object):
    
    @classmethod
    def find_by_permalink(cls, permalink):
        sql = "select * from content where permalink='%s'" % permalink
        results = data.execute_sql(sql=sql)
        content = Content()
        for row in results:
              content.id = row[0]
              content.permalink = row[1]
              content.created = row[2]
        return content
        
    
    def _get_discussions(self):
        """ Return the list of discussions for this piece of content """
        return "" # Discussion.objects.filter(Content=self)
    discussions = property(_get_discussions)


