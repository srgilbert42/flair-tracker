import praw

r = praw.Reddit(user_agent='/u/REDACTED TSM_flair_comment_finder')
already_done = []

while True:
   subreddit = r.get_subreddit('leagueoflegends')
   subreddit_comments = subreddit.get_comments()
   for comment in subreddit_comments:
      if comment.author_flair_css_class == "tsm":
         if comment.id not in already_done: 
            already_done.append(comment.id)
            name = comment.author.name
            submission_title = comment.link_title
            shortened_comment = comment.body[:30]
            string = "[COMMENT] /u/" + name + " in " + "\"" + submission_title + "\" : \"" + shortened_comment + "...\""
            # [COMMENT] /u/REDACTED in "Submission Title" : "Here is my quote"
            print (string)

