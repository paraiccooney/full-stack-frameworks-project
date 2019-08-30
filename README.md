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

## Data Structure
The back-end of this application is built using Postgres (a resource which can be added to Heroku where this app is deployed).  The app uses a relational database type (the comment
section references it's secondary key against the articles primary key).
Hosting of static files is achieved using S3/IAM (AWS Buckets).

## Testing
TO BE COMPLETED

## Deployment
This application is hosted & deployed using Herouku & is located at ( https://paraic-fullstack-project.herokuapp.com/ ). 
The application is currently calibrated to update automatically with new commits as the master origin has been updated to Heroku.

### Obtain the source code
In order to run this application locally you can clone this repository directly into your personal editor using the following command;
git clone (https://git.heroku.com/paraic-fullstack-project.git)
In order for this application to be deployed correctly all html pages which are to be rendered also must be kept
in a folder named 'templates' but can be located anywhere within the directory.
### Install all requirements & create a Superuser (admin)
To successful run this application all packages in the requirements.txt file must be downloaded.  Once this has been completed a superuser must be created in order to gain access
to the built in Django admin panel.  To do this run the following command;
'python3 manage.py createsuperuser' - please note that if Python 3 is your default version 'python3' is to be replaced with 'python'.
Once the superuser has been established append '/admin' to the landing url to access this panel.
### Create your journalists
From within the access panel create a group named 'journalists'.  Add to this group the permission to upload articles.  Add the required registered users to this group (note that
for this step to be completed there must be users in existance).
### Select your platform & create a database
Once you have selected the platform which you wish to run this project on add the database you wish to deploy.  As previously mentioned this app is calibrated for Heroku deployment
& uses the Progress add-on database to store data.  Whatever database you wish to use the database url (located on line 81 of the settings.py file) must be updated.
Should you wish to maintain use of Heroku & Postgres simply set up a Heroku app & add a Postgres database to the app within the resources section.  Alternatively Postgres can
be added to the app using the below command;
'heroku addons:create heroku-postgresql:hobby-dev' - please note that hobby-dev has limited storage capacity.  Please consult the Postgres documentation (https://www.postgresql.org/docs/) 
for further information.
### Set up static & media file hosting
In addition to Postgres we require a storage facility for static files.  Within a test environment files can be hosted locally however for production a more robust database is
required.  We recommend using AWS Cloud based services S3 & IAM to create buckets to store static data.  To achieve this you must have an AWS account (note an AWS Educate
account with not suffice).  Create a bucket within S3 & a policy allowing for public access using IAM.  Attach this policy to the S3 bucket.
For more information here please consult the AWS docs (https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html).

Once this has been completed amend the configuration settings beginning at line 130 of the settings.py file & the custom_storages.py file.
Media files & static files are located in separate folders within the bucket.  In order to update the static files run the below command;
'python3 manage.py collectstatic'
### Setting up Stripe
TBC
### Setting & configuring the environment
For testing an 'env.py' file is recommended which contains all required configuration variables (note that this file must import os).  To switch to another environment comment
out 'import env' within the settings file & set your variables elsewhere (current variables for deployment are set on Heroku in the settings tab).
The required environment variables which are to be set are listed below;
SECRET_KEY
STRIPE_PUBLISHABLE - see the Stripe heading above
STRIPE_SECRET - as above
DISABLE_COLLECTSTATIC - to be set to '1'
EMAIL_ADDRESS - must be a gmail account
EMAIL_PASSWORD
AWS_SECRET_KEY_ID - obtained from within the .csv file during S3/IAM setup
AWS_SECRET_ACCESS_KEY - as above


### Run the application
In order to run the application the below command (we recommend adding an alias to your .bashrc file to create a shortcut for this command);
'python3 manage.py runserver $IP:$C9_PORT'

## Credits
### Content
The content of this application (the articles) were taken for a number of sources listed below;

https://www.bbc.com/news
https://www.inverse.com
https://www.vice.com
https://www.businessinsider.com

### Media
The media for this application (article photos) were taken from the accompanying photos from the above listed sites or from Google Image searches.

## Acknowledgements
The Code Institute community on Slack, my project mentor Aaron Sinnott, & the online tutor support who were of great assistance. 

Stack Overflow was of great use & many contributors had answered questions similar to those I held at separate points throughout the project.











