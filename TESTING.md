## Contents

- [Testing](#testing)
    - [Validator Tests](#validator-tests)
    - [Manual Testing](#manual-testing)
    - [Automated Testing](#python-automated-testing)
- [Bugs](#bugs)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed Bugs](#fixed-bugs)


## Validator Testing

### [PEP8 - CI](https://pep8ci.herokuapp.com/)

|**TEST**|**ACTION**|**EXPECTATION**|**RESULT**|
|-------------------------|---------------------------|---------------------------|-------------|
|**drf-api project** |
|&nbsp;&nbsp;permissions.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/drf-api-project/permissions.PNG) | ✅ |
|&nbsp;&nbsp;serializers.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/drf-api-project/seralizers.PNG)  | ✅ |
|&nbsp;&nbsp;settings.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) |[No issues found](docs/testing-images/drf-api-project/settings.PNG)   | ✅ |
|&nbsp;&nbsp;urls.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) |[No issues found](docs/testing-images/drf-api-project/urls.PNG) | ✅ |
|&nbsp;&nbsp;views.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/drf-api-project/views.PNG)  | ✅ |

|**TEST**|**ACTION**|**EXPECTATION**|**RESULT**|
|-------------------------|---------------------------|---------------------------|-------------|
|**comments** |
|&nbsp;&nbsp;admin.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/comments/admin.PNG) | ✅ |
|&nbsp;&nbsp;apps.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/comments/apps.PNG) | ✅ |
|&nbsp;&nbsp;models.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/comments/models.PNG) | ✅ |
|&nbsp;&nbsp;serializers.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/comments/serializers.PNG) | ✅ |
|&nbsp;&nbsp;urls.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/comments/urls.PNG) | ✅ |
|&nbsp;&nbsp;views.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/comments/views.PNG) | ✅ |

|**TEST**|**ACTION**|**EXPECTATION**|**RESULT**|
|-------------------------|---------------------------|---------------------------|-------------|
|**direct_messages** |
|&nbsp;&nbsp;admin.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/direct-messages/admin.PNG) | ✅ |
|&nbsp;&nbsp;apps.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/direct-messages/apps.PNG) | ✅ |
|&nbsp;&nbsp;models.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/direct-messages/models.PNG) | ✅ |
|&nbsp;&nbsp;serializers.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/direct-messages/serializers.PNG)| ✅ |
|&nbsp;&nbsp;urls.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/direct-messages/urls.PNG) | ✅ |
|&nbsp;&nbsp;views.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/direct-messages/views.PNG) | ✅ |

**TEST**|**ACTION**|**EXPECTATION**|**RESULT**|
|-------------------------|---------------------------|---------------------------|-------------|
|**followers** |
|&nbsp;&nbsp;admin.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/followers/admin.PNG) | ✅ |
|&nbsp;&nbsp;apps.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) |[No issues found](docs/testing-images/followers/apps.PNG)  | ✅ |
|&nbsp;&nbsp;models.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/followers/models.PNG) | ✅ |
|&nbsp;&nbsp;serializers.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/followers/serializers.PNG) | ✅ |
|&nbsp;&nbsp;urls.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/followers/urls.PNG)  | ✅ |
|&nbsp;&nbsp;views.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/followers/views.PNG) | ✅ |

**TEST**|**ACTION**|**EXPECTATION**|**RESULT**|
|-------------------------|---------------------------|---------------------------|-------------|
|**likes** |
|&nbsp;&nbsp;admin.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/likes/admin.PNG) | ✅ |
|&nbsp;&nbsp;apps.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/likes/apps.PNG)| ✅ |
|&nbsp;&nbsp;models.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/likes/models.PNG) | ✅ |
|&nbsp;&nbsp;serializers.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/likes/serializers.PNG) | ✅ |
|&nbsp;&nbsp;urls.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/likes/urls.PNG) | ✅ |
|&nbsp;&nbsp;views.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/likes/views.PNG)| ✅ |

**TEST**|**ACTION**|**EXPECTATION**|**RESULT**|
|-------------------------|---------------------------|---------------------------|-------------|
|**notifications** |
|&nbsp;&nbsp;admin.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/notifications/admin.PNG) | ✅ |
|&nbsp;&nbsp;apps.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/notifications/apps.PNG) | ✅ |
|&nbsp;&nbsp;models.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/notifications/models.PNG)| ✅ |
|&nbsp;&nbsp;serializers.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/notifications/serializers.PNG) | ✅ |
|&nbsp;&nbsp;signals.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/notifications/signals.PNG) | ✅ |
|&nbsp;&nbsp;urls.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/notifications/urls.PNG) | ✅ |
|&nbsp;&nbsp;views.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/notifications/views.PNG) | ✅ |

**TEST**|**ACTION**|**EXPECTATION**|**RESULT**|
|-------------------------|---------------------------|---------------------------|-------------|
|**posts** |
|&nbsp;&nbsp;admin.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/posts/admin.PNG) | ✅ |
|&nbsp;&nbsp;apps.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/posts/apps.PNG) | ✅ |
|&nbsp;&nbsp;models.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/posts/models.PNG) | ✅ |
|&nbsp;&nbsp;serializers.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/posts/serializers.PNG) | ✅ |
|&nbsp;&nbsp;urls.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/posts/urls.PNG)| ✅ |
|&nbsp;&nbsp;views.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/posts/views.PNG) | ✅ |


**TEST**|**ACTION**|**EXPECTATION**|**RESULT**|
|-------------------------|---------------------------|---------------------------|-------------|
|**profiles** |
|&nbsp;&nbsp;admin.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/profiles/admin.PNG) | ✅ |
|&nbsp;&nbsp;apps.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/profiles/apps.PNG)| ✅ |
|&nbsp;&nbsp;models.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/profiles/models.PNG) | ✅ |
|&nbsp;&nbsp;serializers.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/profiles/serializers.PNG) | ✅ |
|&nbsp;&nbsp;urls.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/profiles/urls.PNG)| ✅ |
|&nbsp;&nbsp;views.py | [PEP8 - CI](https://pep8ci.herokuapp.com/) | [No issues found](docs/testing-images/profiles/views.PNG)| ✅ |


## Manual Testing


### Landing Page
| Feature               | Action  | Expected Result                       | Pass/Fail |
|-----------------------|---------|---------------------------------------|-----------|
| **'Sign Up' Button**  | Click   | User is directed to Sign up form      | Pass      |
| **'Sign In' Button**  | Click   | User is directed to the Sign in form  | Pass      |


## Python Automated Testing
Automated testing was conducted on specific components of the application, focusing on key features utilizing Django's built-in 'TestCase' class. Although, given more time the intention was to extend the automated tests to include more features and scenarios. A thourough manual testing process was also implemented.

**Test** | **Description** | **Result** |
|:-----|:------|:------|
|test_inventory_form_valid| Verifies that the "InventoryForm" is validated when provided with a valid category and name. This test ensures that the form's validation logic properly accepts correct input.| Passed
|test_inventory_form_invalid| Tests the "InventoryForm" for correct handling of invalid submissions, specifically when mandatory fields are missing. This test is to confirm that the form's logic handles incomple och incorrect submissions correctly.| Passed
|test_items_form_valid| Verifies that the "ItemsForm" validates correctly when provided with valid data. This test ensures that the form properly handles valid user inputs for item creation.| Passed
|test_items_form_invalid| Test the form handling for invalid submissions, such as when item name is missing.  This test is to confirm that the form's logic handles incomplete och incorrect submissions correctly to prevent data integrity errors.| Passed
|test_create_inventory| Tests the functionality of creating a new inventory list through a POST request, verifying that the list is correctly added to the database and that the user is redirected correctly.| Passed
|test_delete_list| Tests the functionality of deleting an inventory list, verifying that after deletion, the list is deleted from the database and the user redirected correctly.| Passed


## Bugs
The bugs listed below are bugs that I spent a longer amount of time to resolve or that required assistance from Tutor Support. As this is my first Django project, most of the errors and bugs I encountered were learning curves and initial hurdles.

**Bug** | **Description** | **Actions to Resolve** | **Result** |
|:-----|:------|:------|:-----|
|Items didn't get added in the database.|When setting up the inventory form, addition and deletion of items were also handled there. But the items list was empty, the items didn't get added.|Solution: I changed approach and set up a separate form for addition of items.| Resolved
|Itemsform inputfields not working correctly nor the form errors upon sign-up and sign-in. |When editing and adding items, the form wasn't handling the addition of new items correctly. The form errors wasn't working at all upon sign-up and sign-in. User could just proceed even if the requirements weren't met. |Solution: I exchanged widget tweaks to crispy forms and then got it to work properly.| Resolved
|Items didn't get deleted in the front end nor in the database. |When clicking on the delete icon, the delete modal was displayed correctly. When confirmed, a success message would display even though the item wasn't deleted from the list nor in the backend.|Solution: I reached out to tutor support as I spent some time trying to solve this. Finally, changing the class to delete-link instead of delete-icon in the Javascript code fixed the issue.| Resolved
|Clicking on the "Add item" button would display a success message without an item being added. |When clicking on the add item button without adding an item both in the inventory detail view, and in the clone list view, a success message would display.|Solution: I reached out to tutor support as I spent a lot of time trying to solve this. Using length in the inventory detail view to check if an item was added resolved the issue. A check if an item was added or not in the clone list view resolved the issue.| Resolved
|Add category directly in the inventory form not functioning.|I implemented the functionalty to add a new category at the same time as creating the inventory list. This didn't function properly as the input field kept rendering an error.|Solution: I had to change approach since this seemed to complicated to set up. I created a separate page where categories could be added.| Resolved
|A user could see other users categories|During the test phase I discovered that other users' categories would be visible in my category dropdown menu.|Solution: Since the categories are supposed to be personal, and connected to the user, I had to add a user field in my category model to connect the category to the specific user.| Resolved
|A user can create another "General" category.|A "General" category is provided to the user so that the user can choose that category and create a list instantly. A category is unique, same as the inventory name and duplicates can't be created.|Since a "General" category already is provided, the user doesn't have to create that specific category. But in this specific case, the user can create another General category. Due to time constraints and the fact that is not that likey that the user will create another "General" category if one already exists, I choose to leave this issue unresolved for now.| Unresolved
|Duplicate social login buttons|When I added the social media providers in the admin panel, the social login buttons were suddenly duplicated.|Solution: I looked through the relevant templates, debugged and removed code to try and find the source of the problem. Eventually, when I removed the sites, except for the live site I had added in the admin panel the duplicate buttons disappeared.| Resolved
|Scanned QR-code was leading to a relative path|When the QR code was scanned it would only display this path, not leading anywhere: /inventory/153/saved/. When scanned, the saved list view for that specific inventory was supposed to be displayed.|Solution: I did a lot of research and found that Django's reverse function generated a relative path into the QR code instead of the full absolut URL. I modified the method in my Inventory model to return the full absolute URL.| Resolved
|Migration History Error.| InconsistentMigrationHistory. This error occured when I installed the 'django.contrib.sites' framework to add the social account login.| Debugging and deleting records so the order would be correct since that was the cause of the error.| Resolved
|Unique constraint error| Can't clone the original list again due to the uniqe name constraint. To clone a cloned list is working by appending "cloned" to the list name, but if user tried to clone the original list again, an error would occur.|Solution: I added error handling so an error message renders if user tries to clone the original list again.| Resolved
|Mixed content warning| After deployment, the QR-code image wouldn't display and a mixed content warning would appear in the console.|Solution: After a lot of research it became cleare that the issue was about images loaded over HTTP and not HTTPS so I needed to add secure_url to ensure that the image was delivered over HTTPS and that resolved the mixed content warning.| Resolved