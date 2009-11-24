

# 1. Load the Content requested by permalink.
# 2. From the Content load all Discussions.
# 3. From each Discussion load all Posts.
#
# content = Content.find_by_permalink("2004-06-30-World-Class-Supply-Management")
#  # Load the content in the content viewer..
# ..
#  # Annotate the discussions on the content by the discussion.coordinates
# for discussion in content.discussions:
#     # mark content with discussion.coordinates
#
