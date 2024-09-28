# Assignment 2 - Creating Tweeter (A Twitter Clone)

## Author
Joon Lim


## Description

You will be creating a social website called Tweeter that will allow users to
be able to make posts called Twits that other users can view.
Users of the site will be able to make Twits that contain both text and
pictures, follow other users, and like Twits that other users make.

The program should allow the following functionality:

1. Full user authentication so that only authenticated users can use the site.
2. Sign up and authentication forms / views so that users can authenticate with the system.
3. A profile page where a user can update details about themselves including a profile picture.
4. A Dashboad for each user that will show the Twits from followed users with the most recent ones first.
5. A page / form to be able to make a new Twit.
6. New Twits should allow both text and pictures. No need for a text size limit beyond a sensible default.
7. A page for each user that shows all the Twits for that user. Like a public profile so to speak. Similar to dashbaord feed, but only contains all Twits for that specific user.
8. Ability for users to like or unlike a particular Twit that someone has made using AJAX.
9. Ability for users to follow other users. This should use AJAX.
10. Ability for users to comment on Twits that a user has made.


Documentation should include the following for this, and all future assignments:
* Comments at the top of each source code file that you add or edit with:
  * Your Name
  * Class
  * Date
* A comment after the definition of each method describing what it does. I would highly suggest you use the ''' (triple quote) method for the comment.
* Comments in the rest of the code where it isn't obvious what is going on. (I prefer above the line comments vs at the end of the line because who likes to horizontally scroll, but either will work)

Database Requirements:
Here are the requirements for the database in an ERD. There are other authentication related tables that I did not include but are provided via Django's auth system. The Users table is only one that really needed to be shown since there are so many relations between Users and our other tables. There are no relations between the other authentication tables and our tables, which is why I omitted them.

In the in-class we looked up the Images that a user might save by the slug. This slug was determined by converting the title into a slug on save. Since a Twit will not have a title, there is no easy way to generate a slug for it. Instead, you should just rely on the primary key of the Twit model to distinguish one from another. I am expecting you to do some research on your own as to how to accomplish this. Though it is not hard. The documentation site for Django should provide you with what you need as the docs are very good. But if you are stuck, let me know.

![Database Entity Relationship Diagram](http://barnesbrothers.ddns.net/cis218/assignmentImages/cis218_assignment_2_erd.png "Databse Entity Relationship Diagram")

Here are some images of the non-admin pages that I made for my key. This is more or less to give you an idea as to what the general concept is in case the written description is not clear. I realize that your assignment may not end up as elaborate in style as mine, so don't feel as though it needs to visually match mine exactly. I am looking for the general concept though. I will also mention that I used Bootstrap to do my styling.
TODO: Add Images
<!--
![Dashboard](http://barnesbrothers.ddns.net/cis218/assignmentImages/cis218_assignment_2_dashboard.png "Dashboard")
![Profile](http://barnesbrothers.ddns.net/cis218/assignmentImages/cis218_assignment_2_profile.png "Profile")
![Public Profile](http://barnesbrothers.ddns.net/cis218/assignmentImages/cis218_assignment_2_profile.png "Public Profile")
![Twit Creation](http://barnesbrothers.ddns.net/cis218/assignmentImages/cis218_assignment_2_profile.png "Twit Creation")
-->

Solution Requirements:

* Full user authentication so that only authenticated users can use the site.
* Sign up and authentication forms / views so that can authenticate with the system.
* A profile page where a user can update details about themselves including a profile picture.
* A Dashboad for each user that will show the Twits from followed users with the most recent ones first.
* A page / form to be able to make a new Twit.
* New Twits should allow both text and pictures. No need for a text size limit beyond a sensible default.
* A page for each user that shows all the Twits for that user. A public profile so to speak. Similar to dashbaord feed, but only contains all Twits for that specific user.
* Ability for users to like or unlike a particular Twit that someone has made using AJAX.
* Ability for users to follow other users. This should use AJAX.
* Ability for users to comment on Twits that a user has made.

### Notes
Once you have added any additional packages that you need to your project. Be sure to run pip freeze to dump the package information to requirements.txt

  pip freeze > requirements.txt

Remember that you can see all available Bootstrap examples here:

https://getbootstrap.com/docs/4.0/examples/

In addition, you can find the documentation for Bootstrap here:

https://getbootstrap.com/docs/4.0/getting-started/introduction/

## Grading
| Feature                                     | Points |
|---------------------------------------------|--------|
| Full User Authentication and pages          | 15     |
| Personal Profile page                       | 5      |
| Public Profile Tweeter page                 | 10     |
| Dashboard feed of Twits from followed users | 10     |
| New Twit Form                               | 5      |
| Allowing Text and Picture in Twit           | 10     |
| Liking / Unliking a Twit                    | 10     |
| Following / Unfollowing a User              | 10     |
| New Comment Form                            | 10     |
| Styling                                     | 5      |
| Documentation                               | 5      |
| Readme                                      | 5      |
| **Total**                                   | **100**|

## Outside Resources Used
Textbook


## Known Problems, Issues, And/Or Errors in the Program
Adding additional fields to the user model, select related method

