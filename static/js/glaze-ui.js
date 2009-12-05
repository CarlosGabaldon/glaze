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
            
           $("a.load-content").click(this.getContent);
      
        },
        
        getContent: function(){
               var link = $(this)
               $.ajax({
                    type: "GET",
                    url: link.attr("href"),
                    dataType: "json",
                    success: function(content){
                        /*
                        //for testing to view object values.
                         $('#objectViewer').val("Content id: " + content.id + "\r\n" +
                                                 "Content permalink: " + content.permalink + "\r\n" +
                                                 "Content title: " + content.title + "\r\n" +
                                                 "Number of Discussion: " + content.discussions.length + "\r\n" +
                                                 "First discussion coordinates: " + content.discussions[0].coordinates
                                                 );
                        */
                                                 
                         for ( i = 0; i < content.discussions.length; i++ ){
                             a = document.createElement("a");
                             a.setAttribute('href','/discussion/' + content.discussions[i].id);
                             a.setAttribute('class','discussion-topic');
                             t = document.createTextNode('Show Discussion');
                             a.appendChild(t);
                             br = document.createElement("br");
                             $("#margin")
                                .append(a)
                                    .append(br);
                         }
                         
                         $("a.discussion-topic").click(glaze.ui.getDiscussion);
                         
                                         
                         //load the content
                         $.get("/static/content/" + content.permalink + ".html", function(data){
                           $('#contentViewer').attr("innerHTML", data);
                         });
                         
                         //1. annotate the discussion icons on the margin by iterating the discussion.coordinates
                         //2. create <a> tags with permalink of disucssion
                         //3. register event handlers of <a> tags
                         //4. this will be used later to ajax request the disucssion by permalink
                         
                         
                    }
                  });

              return false;
          },
        
        getDiscussion: function(){
            // Get the permalink to the discussion
            //<a class="discussion-topic" href="/discussion/2">Show Discussion</a>
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
            //use microformats..
            html = "<a href='#' id='closeDiscussion'>Close</a><br/>" + 
                   "<h3>Topic: " + discussion.title + "</h3>" +
                   "<textarea cols='60' rows='10'></textarea>";
            
            $('#discussion-popup')
                .toggle()
                    .attr("innerHTML", html);
             
             $('#closeDiscussion').click( function(){
                 $('#discussion-popup').hide();

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