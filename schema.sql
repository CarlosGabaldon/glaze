
# $ mysql -u root < schema.sql
 
drop database if exists glaze;
create database glaze;
use glaze;


CREATE TABLE content (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(200),
  permalink VARCHAR(1000),
  created TIMESTAMP DEFAULT NOW()
);

CREATE TABLE discussion (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  content_id INT,
  topic VARCHAR(200),
  coordinates VARCHAR(100),
  created TIMESTAMP DEFAULT NOW()
);

CREATE TABLE post (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  discussion_id INT,
  posted_by_user_id INT,
  reply_to_post_id INT,
  text TEXT,
  created TIMESTAMP DEFAULT NOW()
);


# A specific piece of content.
INSERT INTO content (title, permalink)
VALUES ("World Class Supply Management", "2004-06-30-World-Class-Supply-Management");
 
# A discussion topic located within the content at a fixed set of
# coordinates. <page>.<word count>, i.e. page 1, 123rd word on page.
INSERT INTO discussion (content_id, topic, coordinates)
VALUES ((SELECT id from content where permalink = '2004-06-30-World-Class-Supply-Management'),"Transformation in Relationships", "01.123"); 

INSERT INTO discussion (content_id, topic, coordinates)
VALUES ((SELECT id from content where permalink = '2004-06-30-World-Class-Supply-Management'),"Transactional Relationships", "02.143"); 

INSERT INTO discussion (content_id, topic, coordinates)
VALUES ((SELECT id from content where permalink = '2004-06-30-World-Class-Supply-Management'),"Supply Managment", "01.123"); 

INSERT INTO discussion (content_id, topic, coordinates)
VALUES ((SELECT id from content where permalink = '2004-06-30-World-Class-Supply-Management'),"On Demand Operations", "02.143"); 


# A post within a discussion.
INSERT INTO post (discussion_id, posted_by_user_id, reply_to_post_id, text)
VALUES ((SELECT id from discussion where topic = 'Transformation in Relationships'), "1", NULL, 
"I am not sure I understand the point about strategic alliance, what does that mean?"); 

INSERT INTO post (discussion_id, posted_by_user_id, reply_to_post_id, text)
VALUES ((SELECT id from discussion where topic = 'Transformation in Relationships'), "2", "1", 
"I think what they are saying is that some relationships in the supply managment chain can change the model.");

INSERT INTO post (discussion_id, posted_by_user_id, reply_to_post_id, text)
VALUES ((SELECT id from discussion where topic = 'Transformation in Relationships'), "1", NULL, 
"This does not clearly state how to deal with a special supply chain operation. 
I think that more thought needs to go into explaining how this will make sense
in a modern tech centered operation."); 

INSERT INTO post (discussion_id, posted_by_user_id, reply_to_post_id, text)
VALUES ((SELECT id from discussion where topic = 'Transactional Relationships'), "2", "1", 
"Please someone explain this section, I am very confussed.");

INSERT INTO post (discussion_id, posted_by_user_id, reply_to_post_id, text)
VALUES ((SELECT id from discussion where topic = 'On Demand Operations'), "2", "1", 
"Where do we get deeper understanding of this point? Mr. Smith would you please explain this section?");

