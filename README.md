# Znapped

The Znapped app is built using Django and is designed to help users efficiently manage their inventories and promote sustainable living. The Znapped
app provides a user-friendly interface for creating, organizing and sharing lists of items. Each list is associated with a unique QR code for easy access and sharing.

The live link can be found here - [znapped-drfapi](https://znapped-drfapi-8eee30ca5ab2.herokuapp.com/)

![Znapped Am I Responsive Image](docs/readme_images/am_i_responsive.png)

## Contents

- [UI/UX](#)
    - [User Stories](#user-stories)
- [Database design](#database-design)
    - [Database Models](#database-models)
- [Testing](#testing)
- [Security Features](#security-features)
- [Technologies & Languages used](#technologies--languages-used)
- [Libraries & Frameworks](#libraries--frameworks)
- [Tools & Programs](#tools--programs)
- [Deployment](#deployment)
    - [Heroku](#heroku)
- [Credits](#credits)
  - [Code](#code)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)



## UX/UI
## User Stories

### User Profile
- As a Site User, I can create an account so that I can start managing my inventories.
- As a Site user, I can verify my account via the verification link sent to my email upon registration.
- As a Site User, I can login to my account so that I can access my existing inventories.
- As a Site User, I can login via Google so that I have several login options.

### User Navigation
- As a Site User I can navigate easily through the site due to a responsive navbar so that I understand where to go and it is always visible to me.
- As a Site User, I can see my lists in a dropdown list from the navigation bar, so that I can navigate to my lists easily.
- As a Site User I can click on the social media links so that I can explore the work of the developer and see the developers profile.

### User Feedback
- As a Site User, I can receive feedback whenever I make an action, so that I know if my action was successful or not.

### Create Inventories
- As a Site User, I can create unique inventory lists so that I can't create inventory lists with the same name.
- As a Site User, I can create an inventory list and add multiple items at once, so that I can organize my belongings efficiently.

### Manage Inventories
- As a Site User, I can generate a QR code for my inventory so that I can identify my belongings easily.
- As a Site User, I can scan the QR code so that I can see my inventory list immediately.
- As a Site User, I can share my inventory with others using the generated QR code so that I can provide a visual and efficient view of the contents of my Inventory to others.
- As a Site User I can clone my lists so that I can reuse a list and just modify it.
- As a Site User, I can see numbers next to the inventory list name so that I can find boxes with an qr code easily if I have many boxes.

### Contact Form
- As a Site User, I can make contact through a contact form, so that I can ask questions, report issues or make suggestions.

### Site Administration
- As a Site owner I can log in to the admin dashboard using my username and password so that I can access the functionalities of the superuser.
- As a Site owner I can view a list of all inventory items so that I can edit, delete or add items, inventories and categories.
- As a Site Owner I can download the QR codes for each inventory so that I can share the QR code with team members.
- As a Site owner I can receive messages submitted through the form so that I can respond to the messages.


## Database Design

### Database Models
The entity relationship diagram provided is the first draft and does not include all the fields and models in the final database.

<details open>
  <summary>Database schema</summary>

  ![Database schema](docs/readme_images/database_schema.png)
</details>

#### User Model (AllAuth)
Django AllAuth was used for the user authentication. The user model handles authentication and representes users in the system. Its function is to store information about users, allowing them to log in and manage their data.

Relationship:

One-to-may relationship with the Inventory Model: One user can have multiple inventories.

#### Inventory Model
The inventory model is managing collections of items. Its function is to organize and store information about inventories created by users. Each inventory is associated with a specific user and can include multiple items. The QR-code image is associated with the inventory.

Relationships:

Many-to-one relationship with the User Model: Many inventories can belong to one user.

One-to-many relationship with the Items Model: One inventory can have multiple items.

Many-to-one relationship with the Category Model: Many inventories can belong to one category.

#### Category Model
Its function is to categorize the inventories. The category model also includes a user field. Categories that was added by other users would be seen by everyone, and that's why I hade to add a user field to link the category to the user. I also choose not to delete the inventory list if a category is deleted. That gives the user the option to change category or delete a list by them self.

Relationship:

Many-to-one relationsship with the Inventory Model: Once category can be associated with multiple inventories.



## Testing
Testing and the results can be found [here](/TESTING.md).

## Security Features

### Form Validation
If empty or incorrect data is added to a form, the form won't submit. An error will arise, informing the user what field caused the error.

### User Authentication
Limits access for non-registred users and permission control so that only the owner of a list can edit and delete a list when shared with others.

### Database Security
- All passwords, API keys, ID:s and the database url are stored in the env.py file to ensure that sensitive information is not shared, along with env.py being listed in the gitignore file.
- CSRF tokens are used on all forms throughout the application.

## Technologies & Languages used

  - HTML5
  - CSS
  - Javascript
  - Python

  - [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Was used throughout the project to make changes and to test the responsivness.
  - [Django](https://docs.djangoproject.com/en/5.0/) - Main python framework for development of this project.
  - [ElephantSQL](https://www.elephantsql.com/) - PostgreSQL database hosting for this project.
  - [Git](https://git-scm.com/) - Git was used for version control by using the Gitpod terminal to commit and then push to Github.
  - [Github](https://github.com/) - Is where the projects code is stored after being pushed.
  - [Gitpod](https://gitpod.io/) - Was the Codespace used for this project.
  - [Heroku](https://www.heroku.com) - The cloud based platform to deploy the site on.

  ## Libraries & Frameworks
  - [Boostrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - Was used to style the app and make it responsive.
  - [Cloudinary](https://cloudinary.com/) - Used to upload the QR-code images.
  - [Crispy-boostrap5](https://pypi.org/project/crispy-bootstrap5/) - To render Django forms in a Boostrap 5 style.
  - [Django-allauth](https://docs.allauth.org/en/latest/) - Authentication library used to create the user accounts.
  - [Django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Used to render the forms.
  - [Django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) - Was used for debugging during the project.
  - [Gunicorn](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/gunicorn/) - Python HTTP server for WSGI applications.
  - [Psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL database adapter for Python.
  - [QRcode](https://django-qr-code.readthedocs.io/en/latest/) -  Used to generate QR codes.
  - [Whitenoise](https://whitenoise.readthedocs.io/en/latest/) - To serve static files directly from Django.

  Additional information is available in the [requirements.txt file](requirements.txt)



   ## Tools & Programs
- [Am I Responsive](https://ui.dev/amiresponsive) - Was used to ensure that the website is responsive on diffrerent devices.
- [Balsamiq](https://balsamiq.com/) - Was used to create the wireframes before starting the project.
- [Font Awesome](https://fontawesome.com/) - Was used for Social Media icons in footer and other icons throughout the application.
- [Google Fonts](https://fonts.google.com/) - Was used to import fonts to the page.

- [JS-hint](https://jshint.com/) - Was used for Javascript Validation.
- [Lucid charts]() - Was used to create the ERD diagrams.
- [PEP-8]() - Was used for Python Validation.
- [Responsinator](http://www.responsinator.com/) - Was also used to ensure that the website is responsive on diffrerent devices.
- [W3C](https://www.w3.org/) - Was used for HTML and CSS Validation.
- [Web Formatter](https://webformatter.com/html) - Was used to make sure the format looks good.
- [WEBP Converter](https://cloudconvert.com/webp-to-png)- Also used to reduce the file size and keep the image quality.
- [TinyPNG](https://jshint.com/) - Was used to reduce the file size and keep the image quality of the background image.


## Deployment

### Heroku
The application was deployed to Heroku using the following steps:

#### Create the Heroku App
1. Log in to Heroku
2. Click on New and select Create new app from the drop-down menu.
3. Enter a unique and appropiate app name.
4. Select you region.
5. Click on "Create App"

#### Create the PostgreSQL database using ElephantSQL
1. Log in to ElephantSQL and navigate to Dashboard.
2. Click on "Create New Instance".
3. Provide a project name and choose "Tiny Turtle", the free plan.
4. Click on "Select Region" and choose Data center.
5. Review all the details and click on "Create Instance".
6. Return to the Dashboard and click on the newly created instance and copy the database URL.

#### Create and prepare files

- Create requirements.txt file
- Create a "Procfile" in the main directory and add: web: gunicorn project-name.wsgi

  ##### Env.py file
  - Create an env.py file in the main directory in your Gitpod workspace and ensure it's included in the .gitignore file.
  - Add the DATABASE_URL and SECRET_KEY to the env.py file.
  - Add the Cloudinary URL to env.py.

  ##### Settings.py file
  - Update the settings.py file to import the env.py file.
  - Add the SECRET_KEY and DATABASE_URL file paths.
  - Comment out the default database configuration.
  - Add Cloudinary to the list of installed apps.
  - Add the settings for STATIC files:
    - The URL
    - Directory path
    - Rooth path
    - Storage path
    - Media URL
    - Default file storage path
  - Link the file to the templates directory in Heroku
  - Change the templates directory to TEMPLATES_DIR
  - Add Heroku to the ALLOWED_HOSTS list

  #### Heroku Config Vars
  Add these Config Vars in Heroku:
  - SECRET_KEY and value
  - CLOUDINARY_URL
  - PORT: 8000
  - DISABLE_COLLECTSTATIC = 1

### Deploy
  - DEBUG in settings.py needs to be set to False before deploying.
  - Navigate to the deploy tab on Heroku and connect to Github and choose your repository.
  - Click on "Enable Automatic Deploys" for automatic deploys or "Deploy Branch" for manual deploys.
  - Click on view or open app to view the deployed site.

### Fork
- Navigate to the repository [Znapped](https://github.com/MilenTecle/Inventory-Manager/tree/main).
- On the right side of the page, at the top of the repository, select "Fork".
- A copy of the repository is now created.

### Clone
1. Navigate to the repository [Znapped](https://github.com/MilenTecle/Inventory-Manager/tree/main).
2. Click on the **'Code'** dropdown menu above the list of files and choose a method to copy the URL, via HTTPS, SSH or GitHub CLI.
3. Open **Terminal**, change the current working directory to the desired location of the cloned directory.
4. Type **'git clone'** and paste the URL copied form GitHub.
5. Type **'Enter'** to create the local clone.




The live link can be found here - [Znapped](https://inventory-manager-milen-aa94458871b4.herokuapp.com/)

## Credits

### Code

#### General
- I Think, Therefore I Blog - I relied on the instructions and walkthrough to setup my project.
- [Integrating Cloudinary-storage](https://dev.to/spymonk/integrating-cloudinary-storage-with-django-4ipb)
- [Django reverse import](https://docs.djangoproject.com/en/5.0/ref/urlresolvers/)
- [Change display name in django admin](https://forum.djangoproject.com/t/django-admin-page-edit-app-names/14720)
- [Debug toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html) - Was used when building the project to further investigate errors.
- [Style the login and signup form](https://github.com/danihodovic/django-allauth-ui) - Style concept was taken from here.

#### Django Authentication System

- [Django authentication system](https://docs.djangoproject.com/en/5.0/topics/auth/default/)

- [Django allauth installation guide ](https://docs.allauth.org/en/latest/installation/quickstart.html)

- [Using Google](https://medium.com/@infowithkiiru/django-user-registration-with-google-67524cce5ab7)
- [Django google oauth](https://pylessons.com/django-google-oauth)

#### Django email authentication
- [Django allauth email](https://florianbgt.com/posts/django_allauth_email_login)
- [email authentication](https://www.codesnail.com/django-allauth-email-authentication-tutorial/?utm_content=cmp-true)


#### QR-code functionality

I used code from here to build the QR-code function:

- [Make a QR-code](https://stackoverflow.com/questions/60404466/can-i-make-a-qrcode-from-a-python-function-with-django)
- [QR-code in django](https://medium.com/@mbrsagor/use-qr-code-in-django-2b5f4c97896)
- [How to generate a QR-code](https://studygyaan.com/django/how-to-generate-a-qr-code-in-django?utm_content=cmp-true)
- [Reading image](https://stackoverflow.com/questions/76900044/issues-reading-image-from-bytesio-object-using-pil)

#### Building the URL
The QR-code image wouldn't display on the deployed site. I encountered a mixed content warning and after a lot of reasearch I understood that I had to make sure the QR code images were loaded securely.


I used these guides and code to solve that problem:
- [Absolute url](https://syntaxfix.com/question/48692/how-can-i-get-the-full-absolute-url-with-domain-in-django)
- [Cloudinary quickstart](https://cloudinary.com/documentation/python_quickstart)
- [Using Cloudinary for image storage](https://www.topcoder.com/thrive/articles/using-cloudinary-for-image-storage-with-express)


#### Clone list
Credit to my mentor Antonio who helped me implement the functionality to clone a list.

#### Empty label
- [Empty label category dropdown](https://stackoverflow.com/questions/37223688/django-empty-label-in-choice-field-no-queryset)

#### Formsets
I used code from here to implement the inline-factory formset:
- [Inline formset](https://stackoverflow.com/questions/29758558/inlineformset-factory-create-new-objects-and-edit-objects-after-created)
- [Django forms](https://docs.djangoproject.com/en/5.0/ref/forms/models/)
- [Formsets](https://docs.djangoproject.com/en/5.0/topics/forms/formsets/)

### For loop counter
To number the inventory lists automatically:
- [For loop counter](https://testdriven.io/tips/f41d2a7e-ee74-4121-bfd5-976f32b9e67a/)

#### Read-only fields

I used code from here to implement the read-only function upon for inline editing:
- [Readonly-fields](https://www.appsloveworld.com/django/100/22/readonly-fields-in-django-formset#google_vignette)
- [Make readonly](https://stackoverflow.com/questions/70340853/how-to-make-some-django-inlines-read-only)


#### Sending email function
I used code from here to setup the sending email function using send_email:

- [send_email](https://docs.djangoproject.com/en/5.0/topics/email/)
- [send_email](https://stackoverflow.com/questions/55156059/how-to-reply-email-from-django-default-admin-to-the-contact)
- [sending emails with gmail](https://cbi-analytics.nl/sending-emails-with-django-1-configuration-and-basics-of-sending-emails-with-gmail/)

#### Share QR-code via email
- [Insert line break](https://stackoverflow.com/questions/22765834/insert-a-line-break-in-mailto-body)

#### Tests
- [Tests](https://testdriven.io/blog/django-custom-user-model/)
- [Transaction atomic](https://docs.djangoproject.com/en/5.0/topics/db/transactions/)

#### Using Boostrap delete confirmation
- [Delete confirmation](https://stackoverflow.com/questions/59566549/how-to-do-delete-confirmation-for-a-table-data-with-bootstrap-modal-in-django)


### Content
The content is written by the developer.


### Media
- The background Image was taken from [iStock](https://www.istockphoto.com/se)

 - I created the logo using [Canva](https://www.canva.com/)


### Acknowledgements
- Antonio, my mentor, for guiding med throughout the project with important suggestions to improve the applications funcionality.
- To the slack community for answering my questions and guiding me.
- To tutor support, for helping me when I got stuck trying to solve problems throughout the project.
- To my husband and family, for all the support and patience throughout this project.