# WordPressPostByEmail

This python script will construct a email from a collection of PLR articles, images and PDF files 
Then it will use the Post by Mail function of WordPress to post the email as a new post in the blog

The email will randomly select on article from a collection of nested folders containing .txt files
It will look at each line of the file and take the top line and set the subject of the email to this.
it will skip a blank line and then write the rest of the content in the .txt file as the body of the
email.

It will then randomly select a graphic immage from a collection of quote posters and attach this to 
the email.

It will then randomly select from a collection of pdf files in a nested folder and attach the pdf to
the email.

it will then send the email to the post by email address for the WordPress site so at the next running of
wp-cron the email will be checked and converted to a post with the subject becoming the title of the post
the body of the email becomming the post body content and the image will be injected into the media library 
and appended to the end of the post. The pdf attachment will be injected into media library and linked from
the body of the post.

Setup of this script will require the host to have created a pop3 email account to recieve the email from 
the script.

A cron job will also need to be created to schedule reliable processing of the waiting emails in the pop3 
account.

As traffic to the site will be unreliable to pull from the email via the wp-cron job function from WordPress.
