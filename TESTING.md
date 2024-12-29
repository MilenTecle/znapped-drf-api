## Contents

- [Testing](#testing)
    - [Validator Testing](#validator-testing)
    - [Manual Testing](#manual-testing)
- [Bugs](#bugs)

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

### Testing API Endpoints and Responses
|**Endpoint** | **Result** |
|-------------------------------|-----------|
| **Profiles**                          |     |
| GET `/profiles/`                          | ✅ |
| GET `/profiles/<pk>/`                     | ✅ |
| PUT `/profiles/<pk>/`                     | ✅ |
| **Posts**                                 |
| GET `/posts/`                             | ✅ |
| POST `/posts/`                            | ✅ |
| GET `/posts/<pk>/`                        | ✅ |
| PUT `/posts/<pk>/`                        | ✅ |
| DELETE `/posts/<pk>/`                     | ✅ |
| **Comments**                              |     |
| GET `/comments/`                          | ✅ |
| POST `/comments/`                         | ✅ |
| PUT `/comments/<pk>/`                     | ✅ |
| DELETE `/comments/<pk>/`                  | ✅ |
| **Likes**                                 |     |
| GET `/likes/`                             | ✅ |
| POST `/likes/`                            | ✅ |
| DELETE `/likes/<pk>/`                     | ✅ |
| **Follower**                              |     |
| GET `/followers/`                         | ✅ |
| POST `/followers/`                        | ✅ |
| DELETE `/followers/<pk>/`                 | ✅ |
| **Messaging**                             |     |
| GET `/direct-messages/`                   | ✅ |
| POST `/direct-messages/`                  | ✅ |
| PATCH `/direct-messages/mark-as-read`     | ✅ |
| DELETE `/direct-messages/<pk>/`           | ✅ |
| **Notifications**                         |     |
| GET `/notifications/`                     | ✅ |
| PATCH `/notifications/mark-as-read`       | ✅ |
| DELETE `/notifications/<pk>`              | ✅ |


### Testing CRUD Operations
**App**|**Create**|**Read**|**Update**|**Delete**|
|------|-------|-----|----|--------|
| **Profiles** | ✅ | ✅ | ✅ | --- |
| **Posts** | ✅ | ✅ | ✅ |  ✅|
| **Comments** | ✅ | ✅ | ✅ |  ✅|
| **Likes** | ✅ | ✅ | --- |  ✅|
| **Followers** | ✅ | ✅ | --- |  ✅|
| **Messaging** | ✅ | ✅ | ✅ |  ✅|
| **Notifications** | --- | ✅ | ✅ |  ✅|



## Bugs
I encountered numerous bugs and errors throughout this project. A lot of the errors and bugs I encountered were learning curves, initial hurdles and typos. Other bugs were related to my CORS_ALLOWED_ORIGINS settings and CSRF_TRUSTED_ORIGINS settings. I also had to downgrade installed packages to resolve issues as eg. images were not displaying.

The images below will display some of the issues resolved:

<details open>
  <summary>Authentication credentials not provided</summary>

  ![Authentication credentials not provided](docs/testing-images/errors/authentication-credentials.PNG)
</details>

<details open>
  <summary>CSRF verification failed</summary>

  ![CSRF](docs/testing-images/errors/CSRF-verification-failed-(403).PNG)
</details>

<details open>
  <summary>Images not displaying</summary>

  ![Images not displaying](docs/testing-images/errors/images-not-displaying.PNG)
</details>

<details open>
  <summary>IntegrityError unique constraint</summary>

  ![IntegrityError](docs/testing-images/errors/Integrity-error-direct-message-model.PNG)
</details>

<details open>
  <summary>IntegrityError receiver_id</summary>

  ![IntegrityError](docs/testing-images/errors/integrity-error-receiver-id.PNG)
</details>

<details open>
  <summary>Page not found</summary>

  ![Page not found](docs/testing-images/errors/page-not-found-notifications.PNG)
</details>