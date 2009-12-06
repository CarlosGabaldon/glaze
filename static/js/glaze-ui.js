(function(){
/*
 *
 * Copyright (c) 2009 Carlos Gabaldon 

 *
 * $Date: 2009-11-30
 */

    var glaze = {};
    

    $(document).ready(function(){

        glaze.ui.init();
        
        
    });
    
    /**
     * Glaze application
     * @class glaze.ui
     */
    glaze.ui = {
        
        init: function(){
            
           glaze.ui.getDiscussionList($("#contentId").attr("href"))
      
        },
        
        getDiscussionList: function(contentId){
            $.ajax({
                    type: "GET",
                    url: "/discussions/" + contentId,
                    dataType: "json",
                    success: function(discussions){
                          
                         for ( i = 0; i < discussions.length; i++ ){
                             
                             discussionLink = "<a href='/discussion/" + discussions[i].id + "'" + 
                                                " class='discussion-topic'>Discussion(" + discussions[i].posts.length  + ")</a> " + 
                                              "<div class='discussion-popup'" + 
                                                   " id='discussionPopup-" + discussions[i].id + "'>s</div>"
                             
                             $("#" + discussions[i].coordinates).append(discussionLink);
                         }
                         
                         $("a.discussion-topic").click(glaze.ui.getDiscussion);
                         
                    }
                  });

              return false;
            
        },
        
  
        getDiscussion: function(){
            //need to not make ajax call if discussion popup is visible...
            $.ajax({
                    type: "GET",
                    url: $(this).attr("href"),
                    dataType: "json",
                    success: function(discussion){              
                        glaze.ui.loadDiscussionWindow(discussion);
                    }
                  });
            
            return false;
        },
        
        newDiscussion: function(){
            
        },
           
        loadDiscussionWindow: function(discussion){
            
            //build posts list..
            post_html = "<ol>";
            for ( i = 0; i < discussion.posts.length; i++ ){
                post_html = post_html + 
                    "<li><span id='" + discussion.posts[i].id + "'>" + 
                    discussion.posts[i].text +"</span></li>"
            }
            post_html = post_html + "</ol>";
            
            html = "<a id='closeDiscussion'>Close</a><br/>" + 
                   "<h4>Topic: " + discussion.title + "</h4>" +
                   post_html +
                   "<form  action='' method='post'>" +
                        "<textarea id='post' name='post' cols='60' rows='10' class='comment'></textarea>" +
                        "<br/><br/>" +
                       "<input type='submit' value='Post'  />" +
                   "</form>";
            
            $('#discussionPopup-' + discussion.id)
                .toggle()
                    .attr("innerHTML", html);
             
             $('#closeDiscussion').click( function(){
                 $('#discussionPopup-' + discussion.id).toggle();

             });
             
            
        },
        
        postComment: function(comment, url, callback){
            
            $.ajax({
              type: "POST",
              url: url,
              data: $.param({ comment: comment }),
              success: callback
            });
            
        }

    };
        
    
})();