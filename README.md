# [Full Stack Frameworks Project](https://paraic-fullstack-project.herokuapp.com/)
This is an interactive web application with both front-end & back-end functionality.  It constitutes the fourth of my four projects which form the assessment 
basis of my Full-Stack Web Development course with The Code Institute.
The purpose of this project is to allow users to interact with a back-end database of new articles using an appealing & intuitive front-end.  The application
allows users to upload & save comments if they are registered & logged in & to upload articles should they be given the permission to do so through Django's user groups functionality.
The application also serves the purpose of allowing the administrator to attract revenue through donations.

## Notice to the administrator
This app is designed to interact with three types of user;
1. An unregistered user.  These users have the capacity to view articles but cannot comment or donate.
2. A registered user.  These users have the additional capacity to comment on articles.
3. Writers.  These users have the ability to upload Articles to the database via access to an additional form.  In order to manage this group you must create a user group called
'journalists' from within the admin panel (this can only be done by the superuser - see Deployment section below) & manually add the desired user to this group.

## UX
The design goal of this project was to make the front-end as intuitive as possible while also providing a professional & serious display which serves to display authority.
The Bootswatch theme 'Lux' was used to achieve this & the design of different elements throughout the website remains consistant with the nature of this theme.

Interaction with the highest level of the back-end is done using the built-in Django admin panel.  I chose to maintain this functionality as it is very intuative & practical.
For general users interaction with the back-end is maintained using the comment form from within the full-article view (provided the users is registered & authenticated).
For users who have been granted permission to create articles (those who have been added to the 'journalists' group by the superuser) interaction with the back-end is maintained
using a custom built form (the 'write' tab present in the Nav should a user be present in the appropriate group).  The decision to create a custom form (as opposed to a pre-existing
Django form) was made to maintain the professional feel of the site for the journalists.  It was established that to break from this & to allow journalists to view the Django default
back-end would be detrimental to the professionalism of the application.

This app has been built using mobile-first principals.  The site is fully responsive - thanks in a large part to Bootstraps features but also due to the media queries present in the
CSS.  The max height of the article divs was also extended to allow for full content rendering on mobile devices.


## Technologies Used
1. HTML
2. CSS
3. Bootswatch/Bootstrap
4. Materialize
5. Javascript
6. jQuery
7. Python
8. Django
9. Jinja2
10. Postgres
11. Stripe
12. S3/IAM (AWS Buckets)

## Features
**Feature 1 - Registration & Authentication**
The application makes use of Djangos build in authentication functionality.  As can be seen within the Navbar upon entering the site the options to register of log-in are provided.
Users are also promted to sign in should they wish to comment or donate.  Authentication is used to determine what is rendered within the HTML & therefore is used to established
what the user can interact with.

**Feature 2 - Django Groups **
As previously mentioned this application makes use of Djangos group functionality.  A group has been created from within the admin panel named 'journalists'.  Registered users
are then added to this group should the administrator wish them to have the capability to upload articles to be view by other visitors/users or the site.  Rendering the 'write'
option is controlled from within the url views where it is determined if the user is a member of the 'journalists' group.  Should this be the case a variable is passed into the
rendering dictionary with a value or true.  Should this not be the case this variable is set to false.  Jinja then rendered based on this booleen value.

**Feature 3 - Stripe/Payment Functionality **
This application makes use of the Stripe API in order to process electronic payments.  These payments (in the form of donations) are to be used by the administrator to generate
revenue.  The Stripe API connected via the stripe.js file which can be seen from within the static/js folder.  The inputs passed to Stripe for processing are established using
Djangos forms & models (of which some values are obtained by passing these forms into the donate.html page) & passed from within the donate/views.py file.

**Feature 4 - Search Functionality **
The application impliments search capabilities.  This is done from with the search app which is then imported into the main project (newspaper).  Search input is referenced against
headlines, tags (which are metadata invisible to readers), & author names.  Searches do not have to be an exact match.

**Feature 5 - Article Views **
There are two main views available to the user (excluding the journalists) - the all-articles page & the full-article page.  By default the landing page which a
user will come across will be index.html which will render all articles present in the database.  These are filtered in descending order to allow the most recent articles to
be displayed first.
The second view is that which displays fullarticle.html.  This view takes the primary key as an argument in order to render the selected article.  This primary key is also
passed into the comments database to return those comments which apply to that particular article.  As previously mentioned it is also possible within the view to submit a comment
should the user be logged in.

### Features Left to Implement
** Pagination **
As the site grows & additional articles are uploaded it would not be practical to display all entries on the home page or on the search results page should the search return many
results.  As a result I would impliment pagination using Bootstrap while keeping in line with the Bootswatch 'Lux' theme.

** Journalist Dashboard **
I believe it would be useful for journalists to have access to certain metrics on their articles which are displayed in an institive manner.  A dashboard can be implimented which
would provide stats such as a view trend over time, interactive uptake (rate of comments), & possibly the correlation data between these metrics & the tags used.
Crossfilters & D3 could be utilised to construct this dashboard.

** Top articles or custom sort **
At present articles are displayed based on their published date.  As the database grows I believe it would be benefical to add functionality to allow users to view articles
based on different metrics such as 'most-commented' or 'most-viewed' articles of the past day or week.












