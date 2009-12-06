
# $ mysql -u root < schema.sql
 
drop database if exists glaze;
create database glaze;
use glaze;


CREATE TABLE content (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(200),
  permalink VARCHAR(1000),
  body TEXT,
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
INSERT INTO content (title, permalink, body)
VALUES ("World Class Supply Management", 
        "2004-06-30-World-Class-Supply-Management",
        "<p id='01123'>
          In this section of the book, we describe and discuss five key concepts which both enable and facilitate World Class Supply ManagementSM. These concepts underlie and enable two or more phases of the supply management process. Chapter 5 describes the three fundamental types of relationships which exist between professional buyers and suppliers: transactional, collaborative, and alliance. Although these relationship types are implicitly straightforward, supply managers often have varying definitions of them. The result? A term such as “partnership” has been misinterpreted so frequently, we have chosen to purge it from this book. Many of us have heard the story of the sales manager who charged his sales force to establish partnerships & whatever that means. The salespeople, in turn, informed their customers that they wanted to establish partnerships, with little or no understanding of the implications to both parties.
        </p>
        <p>
          World-class supply managers recognize that there is a time and a place for transactional, collaborative, and alliance buyer-supplier relationships. They know the strengths and weaknesses of each type of relationship and design their “relationship strategy” so as to maximize the return on the available investment in human resources. There is no question that well-developed and well-managed alliances deliver the optimum in the areas of cost, quality, time to market, technology flow, and continuity of supply. But such relationships require a significant investment in human resources. Based on anecdotal evidence, we recommend that buyer-supplier relationships evolve through a collaborative phase before blooming into alliances. Unfortunately, most alliances appear to be doomed to failure unless the strategic objectives of the two firms are properly aligned; there is a compatibility of corporate cultures; and institutional trust is developed and maintained.
        </p>
        <p id='01233'>
          Supply management is the most interdisciplinary of all functions. It cuts across department lines and requires the involvement of many disciplines. Thus, it is essential that the professional supply manager possess or develop cross-functional team participation and leadership skills. Chapter 6 introduces several key teaming concepts which will assist all members of an organization's supply management system to maximize the system's contribution to the firm's bottom line. These concepts apply equally within the firm and with interfirm teams. Careful application of these concepts and practices will help all members of the supply management system to properly balance their personal workload between functional and cross-functional activities.
        </p>
        <p>
          It is our belief that no other functional area or system has more impact on the quality of the organization's products and services than does supply management. Experience indicates that some 75 percent of field failures can be traced back to defects in purchased materials. Chapter 7, Quality Management, demonstrates that there are many approaches to proactively mitigating quality problems. The chapter describes several philosophies, approaches, tools, and methodologies that supply management may perform in order to eliminate or minimize defects throughout its supply chains. The focus of the chapter is on developing quality design and prevention systems rather than reactive detection systems.
        </p>
        <p id='01143'>
          Some 40 years ago, the U.S. Air Force introduced the concept of life cycle costing. Instead of addressing operating characteristics and flyaway costs only, we analyzed the cost of owning and operating a weapon system over its expected life. The private sector has learned much from the Department of Defense in what has come to be known as the Total Cost of Ownership. We believe that every supply manager, every program manager, every design engineer—in fact, every decision maker—must be familiar with and support the principles described in Chapter 8, Total Cost of Ownership.
        </p>
        <p id='01322'>
          The last chapter of this section is entitled e-Commerce II. Much as MRP laid the foundation for MRPII, we believe that e-Commerce, with its focus on impersonal electronic systems, must evolve to a more realistic approach: e-Commerce II. e-Commerce II goes beyond the transactional capabilities of electronic commerce to fulfill strategic goals across supply chains. It is our belief that electronic commerce is adapting to facilitate long-term collaborative relationships and provide synergistic rewards that could not be obtained through e-Commerce I. As will be presented in this chapter, two key missing ingredients in e-Commerce I were trust and the human element in buyer-supplier relationships. World Class Supply ManagementSM calls for trust to be developed between supply chain members. Trust as presented by WCSM is developed between individuals who can have an open dialog on real issues and possible solutions. Only then can e-Commerce II succeed in providing open sharing of information across company boundaries to enable the potential for optimization of the supply chain. As seen throughout this book, e-Commerce II is an enabler, not a replacement, of the essential human aspect of buyer-supplier relationships.
        </p>");
 
# A discussion topic located within the content at a fixed set of
# coordinates. <page>.<word count>, i.e. page 1, 123rd word on page.
INSERT INTO discussion (content_id, topic, coordinates)
VALUES ((SELECT id from content where permalink = '2004-06-30-World-Class-Supply-Management'),"Transformation in Relationships", "01123"); 

INSERT INTO discussion (content_id, topic, coordinates)
VALUES ((SELECT id from content where permalink = '2004-06-30-World-Class-Supply-Management'),"Transactional Relationships", "01143"); 

INSERT INTO discussion (content_id, topic, coordinates)
VALUES ((SELECT id from content where permalink = '2004-06-30-World-Class-Supply-Management'),"Supply Managment", "01233"); 

INSERT INTO discussion (content_id, topic, coordinates)
VALUES ((SELECT id from content where permalink = '2004-06-30-World-Class-Supply-Management'),"On Demand Operations", "01322"); 


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

