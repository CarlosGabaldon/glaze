
#Gets forum list from user_api_key which will return the forum_id need to get the comments for that discussion.
curl -0 -L "http://disqus.com/api/get_forum_list?user_api_key=wwVWtbICyVGySXjlektHye8R0wIHkMoCgdRSVFOdpMeVTkTbH2k8bMQidoAfuXjX&api_version=1.1" 


# Gets forum posts from user_api_key and form_id from above call.
curl -0 -L "http://disqus.com/api/get_forum_posts?user_api_key=wwVWtbICyVGySXjlektHye8R0wIHkMoCgdRSVFOdpMeVTkTbH2k8bMQidoAfuXjX&forum_id=479516&api_version=1.1" 