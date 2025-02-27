# Znapped API

Znapped API is built using Django REST Framework. It serves as the API for a social media platform where users can create posts, follow other users, react to content, comment, send direct messages and manage notifications.

![Znapped-drf-api](docs/readme-images/znapped-drfapi.PNG)


Live Links
- Backend live API: [Znapped API](https://znapped-drfapi-8eee30ca5ab2.herokuapp.com/)
- Frontend live Site: [Znapped](https://znapped-972f129d36da.herokuapp.com/)

- Frontend repository: [Frontend repository](https://github.com/MilenTecle/znapped)

## Contents

- [Features](#)
    - [User Management](#user-management)
    - [Content Management](#content-management)
    - [Messaging](#messaging)
    - [Notifications](#notifications)
    - [Search and Filter](#search-and-filter)
- [API Endpoints](#api-endpoints)
    - [User and Profile](#user-and-profile)
    - [Posts](#posts)
    - [Comments](#comments)
    - [Likes](#likes)
    - [Follower](#follower)
    - [Messaging](#messaging)
    - [Notifications](#notifications)
- [Database Models](#database-models)
    - [User model](#user-model)
    - [Profile model](#profile-model)
    - [Post model](#post-model)
    - [Comment model](#comment-model)
    - [Like model](#like-model)
    - [Follower model](#follower-model)
    - [Direct Message model](#direct-message-model)
    - [Notification model](#notification-model)
- [Testing](#testing)
- [Technologies](#technologies)
- [Libraries & Frameworks](#libraries-frameworks)
- [Deployment](#deployment)
    - [Heroku](#heroku)
- [Credits](#credits)
  - [Code](#code)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)



## Features

### User Management
- User profiles with custom fields.
- User authentication using JWT.
- Follow and unfollow functionality

### Content Management
- Create, edit delete posts with images, hashtags and mentions.
- Add, edit and comments on posts.
- React to posts with different reaction types (heart, thumbs up, happy, sad, angry).

### Messaging
- Direct messages between users with read status tracking.
- Notifications for new messages.

### Notifications
- Notifications for likes, follows, comments and messages.
- Mark notifications as read.

### Search and Filter
- Search functionality for posts, hashtags and users.
- Filter posts by likes, comments, hashtags and followers.

## API Endpoints

### User and Profile
- GET `/profiles/` - List all user profiles
- GET `/profiles/<pk>/` -  Retrieve a single profile
- PUT `/profiles/<pk>/` - Update profile details, only for authenticated users.

### Posts
- GET `/posts/` - List all posts
- POST `/posts/` - Create a new post
- GET `/posts/<pk>/` - Retrieve a specific post
- PUT `/posts/<pk>/` - Update a post (owner only)
- DELETE `/posts/<pk>/`- Delete a post (owner only)

### Comments
- GET `/comments/` - List all comments
- POST `/comments/` - Create a comment
- PUT `/comments/<pk>/` - Update a comment (owner only)
- DELETE `/comments/<pk>/` - Delete a comment (owner only)

### Likes
- GET `/likes/` - List all likes
- POST `/likes/` - React to a post
- DELETE `/likes/<pk>/` - Remove a reaction (owner only)

### Follower
- GET `/followers/` - List all followers
- POST `/followers/` - Follow a user
- DELETE `/followers/<pk>/` -Unfollow a user (owner only)

### Messaging
- GET `/direct-messages/` - List all messages
- POST `/direct-messages/` - Send a message
- PATCH `/direct-messages/mark-as-read` - Mark messages as read.
- DELETE `/direct-messages/<pk>/` - Delete a message (Sender or receiver)

### Notifications
- GET `/notifications/` - List all notifications
- PATCH `/notifications/mark-as-read` - Mark notifications as read.
- DELETE `/notifications/<pk>` - Delete a notification (owner only)


## Database Models
The entity relationship diagram provided is the first draft and does not include all the fields and models in the final database.

<details open>
  <summary>Database schema</summary>

  ![Database schema](docs/database-schema/Database-schema.png)
</details>

#### User Model
Handles user authentication and user management.

Relationships:
- One-to-one relationship with the Profile model.
- One-to-many relationship with the Post, Comment, DirectMessage, Like and Follower models.

#### Profile Model
Represents a user's profile with additional information like, bio, image, post and follower count.

Fields:
- owner (One-to-one with User)
- name
- content
- image
- followers_count
- following_count
- post_count.

Relationships:
- One-to-one relationship with the User model.
- Connected to Follower Model via the User model to link followers and following.

#### Post Model
Represents user-generated posts, including support for images and hashtags.

Fields:
- title
- content
- image
- hashtags
- mentions
- created_at
- updated_at

Relationships:
- Many-to-one relationship with the User model.
- One-to-many relationship with the Comment and Like models.
- Many-to-many relationship with the Hashtag model

#### Comment Model
Represents a comment on a post.

Fields:
- content
- post
- mentions
- owner
- created_at
- updated_at

Relationships:
- Many-to-one relationship with the User model.
- Many-to-one relationship with the Post model.
- Many-to-many relationship with the User model (for mentions).

#### Like Model
Represents a reaction to a post.

Fields:
- owner
- post
- reaction_type
- created_at

Relationships:
- Many-to-one relationship with the User model.
- Many-to-one relationship with the Post model.

#### Follower Model
Represents a user following another user.

Fields:
- owner
- followed
- created_at

Relationships:
- Many-to-one relationship with the User model (as owner)
- Many-to-one relationship with the User model (as followed)

#### Direct Message Model
Represents a private message between users.

Fields:
- sender
- receiver
- content
- read
- created_at
- updated_at

Relationships:
- Many-to-one relationship with the User model (as sender).
- Many-to-one relationship with the User model (as receiver).
#### Notification Model
Tracks notifications for user activities such as likes, messages and mentions.

Fields:
- type
- message
- user
- sender
- post
- message_id
- created_at
- read

Relationships:
- Many-to-one relationship with the User model (as user and sender)
- Many-to-one relationship with the DirectMessage model.

## Testing
Testing and the results can be found [here](/TESTING.md).


## Technologies

   - [Microsoft Edge Dev Tools](https://learn.microsoft.com/en-us/microsoft-edge/developer/) - Was used throughout the project to make changes and to test the responsiveness.
  - [Django](https://docs.djangoproject.com/en/5.0/) - Main python framework for development of this project.
  - [ElephantSQL](https://www.elephantsql.com/) - PostgreSQL database hosting for this project.
  - [Git](https://git-scm.com/) - Git was used for version control by using the Gitpod terminal to commit and then push to Github.
  - [Github](https://github.com/) - Is where the projects code is stored after being pushed.
  - [Gitpod](https://gitpod.io/) - Was the Codespace used for this project.
  - [Heroku](https://www.heroku.com) - The cloud based platform to deploy the site on.
  - [JWT](https://jwt.io/introduction) - Used for authentication

  ## Libraries & Frameworks
  - [Cloudinary](https://cloudinary.com/) - Used for media storage
  - [Django-allauth](https://docs.allauth.org/en/latest/) - Authentication library used to create the user accounts.
 the project.
  - [Gunicorn](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/gunicorn/) - Python HTTP server for WSGI applications.
  - [Psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL database adapter for Python.
  - [Whitenoise](https://whitenoise.readthedocs.io/en/latest/) - To serve static files directly from Django.

  Additional information is available in the [requirements.txt file](requirements.txt)

## Deployment

### Heroku
The application was deployed to Heroku using the following steps:

#### Create the Heroku App
1. Log in to Heroku
2. Click on New and select Create new app from the drop-down menu.
3. Enter a unique and appropriate app name.
4. Select you region.
5. Click on "Create App"

#### Create the PostgreSQL database
Use the [CI Database Maker](https://dbs.ci-dbs.net/) provided by Code Institute to create you PostgreSQL database.

Or create the database using ElephantSQL:
1. Log in to ElephantSQL and navigate to Dashboard.
2. Click on "Create New Instance".
3. Provide a project name and choose "Tiny Turtle", the free plan.
4. Click on "Select Region" and choose Data center.
5. Review all the details and click on "Create Instance".
6. Return to the Dashboard and click on the newly created instance and copy the database URL.

  #### Heroku Config Vars
  1. Go to the settings tab and navigate to config vars.
  2. Click to reveal config vars and add the database url.
  3. Add config var: DATABASE_UR and value: the PostgreSQL database url.
  4. Add config var: DISABLE_COLLECSTATIC and the value: 1.


#### Create and prepare files

- Create requirements.txt file
- Create a "Procfile" in the main directory and add:
**release: python manage.py makemigrations && python manage.py migrate
web: gunicorn drf_api.wsgi**

### Install libraries
- Install DJ Database by using the command - pip install dj_database_url in the terminal.
- Install gunicorn by using the command - pip install gunicorn in the terminal.
- Install CORS by using the command pip install django-cors-headers.

  ##### Env.py file
  - Create an env.py file in the main directory in your Gitpod workspace and ensure it's included in the .gitignore file.
  - Add the DATABASE_URL to the env.py file and the rest of your variables.

  ##### Settings.py file
  - Update the settings.py file to import the env.py file and import dj_database_url.
  - Add the SECRET_KEY and DATABASE_URL file paths.
  - Replace the default database configuration.
  - Add Heroku and localhost to the ALLOWED_HOSTS list.
  - Add 'corsheaders' to the installed apps and 'corsheaders.middleware.CorsMiddleware' at the top of the Middleware list.
  - To allow cookies, add CORS_ALLOW_CREDENTIALS = True.
  - Add your local and deployed url to CORS_ALLOWED_ORIGINS.

### Deploy
  - DEBUG in settings.py needs to be set to False before deploying.
  - Navigate to the deploy tab on Heroku and connect to Github and choose your repository.
  - Click on "Enable Automatic Deploys" for automatic deploys or "Deploy Branch" for manual deploys.
  - Click on view or open app to view the deployed site.

### Fork
- Navigate to the repository [Znapped API](https://github.com/MilenTecle/znapped-drf-api).
- On the right side of the page, at the top of the repository, select "Fork".
- A copy of the repository is now created.

### Clone
1. Navigate to the repository [Znapped API](https://github.com/MilenTecle/znapped-drf-api).
2. Click on the **'Code'** dropdown menu above the list of files and choose a method to copy the URL, via HTTPS, SSH or GitHub CLI.
3. Open **Terminal**, change the current working directory to the desired location of the cloned directory.
4. Type **'git clone'** and paste the URL copied form GitHub.
5. Type **'Enter'** to create the local clone.



## Credits

### Code

#### General
- The Django REST Framework walkthrough project served as the foundation of my backend project.

#### Notifications
 General guidance on how to implement a Notifications System:
- [How to implement Notifications System](https://stackoverflow.com/questions/72264677/how-can-i-implement-notifications-system-in-django)

Models and APIs to mark notifications as read:
- [Real-Time Notification System](https://www.horilla.com/blogs/how-to-build-a-real-time-notification-system-with-django-notifications-hq/)

- [Django Server-Sent Events](https://keepsimple.dev/p/django-server-sent-events.html)

- [Notification Types and signal implementation](https://dev.to/m16bappi/building-a-flexible-notification-system-in-django-a-comprehensive-guide-571g)

Using signals for notifications:
- [Django signals documentation](https://docs.djangoproject.com/en/5.1/topics/signals/)

- [Setup and triggering of signals](https://stackoverflow.com/questions/64666741/why-is-my-signal-not-working-in-django-what-im-doing-wrong)

#### Direct Messages
Query logic in DirectMessage views:
- [Query Optimization with Django Rest Framework](https://tech.serhatteker.com/post/2021-11/django-rest-query-part-2/)

- [Django Queries Documentation](https://docs.djangoproject.com/en/5.1/topics/db/queries/)

- [Complex Lookups with Q Objects](https://docs.djangoproject.com/en/5.1/topics/db/queries/#complex-lookups-with-q-objects)

Implementation of Messaging System:
- [Django Messages Framework Documentation](https://docs.djangoproject.com/en/5.1/ref/contrib/messages/)

- [Django DirectMessages structure](https://codemax.app/snippet/implementation-of-django-directmessages-application)

- [Private Messaging Conversation View](https://stackoverflow.com/questions/43696074/django-private-messaging-conversation-view)

#### Hashtags
- [Creating and associating Hashtags](https://stackoverflow.com/questions/28274333/django-rest-framework-many-to-many-relations-create-if-not-exists)

Detailed guides on how to serialize Many-to-Many fields and update a Many-to-Many Relationship that I used when implementing the hashtag functionality and logic to associate hashtags:
- [How to serialize Many-to-Many Fields](https://codemax.app/snippet/how-to-serialize-the-many-to-many-fields-in-drf)

- [Updating a Many-to-Many Relationship](https://dev.to/danielcoker/updating-a-many-to-many-relationship-5h2j)

- [Django REST Framework Serializers Documentation](https://www.django-rest-framework.org/api-guide/serializers)

- [Implementing Tags (StackOverflow)](https://stackoverflow.com/questions/50203063/implementing-tags-using-django-rest-framework)

List processing and extraction of hashtags:
- [List processing and extraction of items (hashtags)](https://stackoverflow.com/questions/50203063/implementing-tags-using-django-rest-framework)

- [Extract hashtags from a post](https://stackoverflow.com/questions/68918228/django-extract-hash-tags-from-a-post-and-save-them-all-in-a-many-to-one-relati)

### Content
The content is written by the developer.


### Acknowledgements
- Jubril, my mentor, for guiding med throughout the project with important suggestions and invaluable support to improve the applications functionality.
- To the slack community for answering my questions and guiding me.
- To tutor support, for helping me when I got stuck trying to solve problems throughout the project.
- To my husband and family, for all the support and patience throughout this project.

[Back to the top](<#contents>)