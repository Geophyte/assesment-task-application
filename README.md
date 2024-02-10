# Documentation

## Setup
For the setup, we need to create a virtual Python environment with `python -m venv venv`, then we need to install requirements using `pip install -r requirements.txt`.
After setting up the virtual environment, we execute `cd backend` and `python manage.py runserver`.
We can populate the database using `python generate_data.py`.

## Endpoints
- `/admin/` - A standard Django admin panel. **WARNING:** Using it to modify/create data might bypass API's data validation.
- `/register/` - **POST:** Registers the user. **GET:** Retrieves the registration HTML form. Users cannot be logged in when accessing this endpoint. This endpoint does not automatically log in the user upon registration.
- `/login/` - **POST:** Logs in the user. **GET:** Retrieves the login HTML form. Users cannot be logged in when accessing this endpoint. Username and password are required for login.
- `/logout/` - **POST:** Logs out the user. **GET:** Retrieves the logout HTML form. Users must be logged in when accessing this endpoint.
- `/whoami/` - **GET:** Retrieves information about the currently logged-in user.
- `/users/` - Allows safe methods (GET, HEAD, OPTIONS) for everyone. Logged-in users can delete/modify only their profiles. Creating new users must be done through `/register/`.
- `/categories/` - Allows safe methods (GET, HEAD, OPTIONS) for everyone. Logged-in users can create/delete categories. Categories must have unique names.
- `/tasks/` - Allows safe methods (GET, HEAD, OPTIONS) for everyone. Logged-in users can create/delete/modify tasks. Tasks must have a unique title-category pair.
- `/comments/` - Allows safe methods (GET, HEAD, OPTIONS) for everyone. Logged-in users can create comments. Logged-in users can delete/modify only their comments.

## Accessing API endpoints:
These requests might require a CSRF token for some of the requests. Paging is enabled so endpoints returning lists will return 10 objects. To access other pages, we need to add `?page=<page_number>`.

### Unlogged-in user
1. **GET** `<server_url>/<users | categories | tasks | comments>/` - Returns the first 10 `<users | categories | tasks | comments>`.
2. **GET** `<server_url>/<users | categories | tasks | comments>/<object_id>/` - Returns `<users | categories | tasks | comments>` with `object_id` as id.
3. **GET** `<server_url>/comments/user/<user_id>/` - Returns comments from specified `user_id`.
4. **GET** `<server_url>/comments/task/<task_id>/` - Returns comments with specified `task_id`.
5. **GET** `<server_url>/comments/user/<user_id>/task/<task_id>/` or `<server_url>/comments/task/<task_id>/user/<user_id>/` - Returns comments from specified `user_id` and with `task_id`.
6. **POST** `<server_url>/register/` - Registers the user. The body must contain 'username' (string), 'email' (string), and 'password' (string) fields.
7. **POST** `<server_url>/login/` - Logs in the user. We get CSRF token and session id. The body must contain 'username' (string) and 'password' (string) fields.

### Logged-in user
1. **GET** `<server_url>/<users | categories | tasks | comments>/` - Returns the first 10 `<users | categories | tasks | comments>`.
2. **GET** `<server_url>/<users | categories | tasks | comments>/<object_id>/` - Returns `<users | categories | tasks | comments>` with `object_id` as id.
3. **POST** `<server_url>/categories/` - Allows us to create a category. Body must contain 'name' (string) field.
4. **DELETE** `<server_url>/categories/<category_id>/` - Allows us to delete a category.
5. **POST** `<server_url>/tasks/` - Allows us to create a task. Body must contain 'title' (string), 'description' (string), 'completed' (true/false), and 'category' (numerical, category_id) fields.
6. **PATCH** `<server_url>/tasks/<task_id>/` - Allows us to modify an existing task. Body must contain at least one of these fields: 'title' (string), 'description' (string), 'completed' (true/false), 'category' (numerical, category_id).
7. **DELETE** `<server_url>/tasks/<task_id>/` - Allows us to delete a task.
8. **POST** `<server_url>/comments/` - Allows us to create a comment. Body must contain 'text' (string) and 'task' (numerical, task_id) fields.
9. **PATCH** `<server_url>/comments/<comment_id>/` - Allows us to modify a comment belonging to the current user. Body must contain at least one of these fields: 'text' (string), 'task' (numerical, task_id).
10. **DELETE** `<server_url>/comments/<comment_id>/` - Allows us to delete a comment belonging to the current user.
11. **GET** `<server_url>/whoami` - Retrieves information about the currently logged-in user.
12. **PATCH** `<server_url>/users/<user_id>/` - Allows us to modify a user profile belonging to the current user. Body must contain at least one of these fields: 'username' (string), 'email' (string), 'profile_picture' (image file) fields.
13. **PATCH** `<server_url>/users/<user_id>/delete_profile_picture/` - Allow us to delete user profile picture and set it to null
14. **DELETE** `<server_url>/users/<user_id>/` - Allows us to delete a user profile belonging to the current user.
15. **POST** `<server_url>/logout/` - Allows us to logout and end session for current user.


# Technical Task: Django Application with Docker and DRF

## Objective:
Create a Django application with models, migrations, and API endpoints using Django Rest Framework (DRF). Dockerize the application for easy deployment.

## Requirements:

### Django Application:
- Create a Django project.
- Implement two models: ex: Task and Category.
- Task should have fields: id (auto-generated), title, description, completed (boolean), and category (foreign key to Category model).
- Category should have fields: id (auto-generated), and name.
- Feel free to use your own subject area.
- Feel free to make it more complex to demonstrate your skills.

### Django Migrations:
- Create Django migrations for the models.
- Apply the migrations to create the database schema.
- Setup admin pages for those models.

### Django Rest Framework (DRF):
- Use DRF to create API endpoints for the Task and Category models.
- Implement CRUD operations for both models (Create, Read, Update, Delete).
- Ensure that the API is properly authenticated, and only authenticated users can perform write operations (create, update, delete).

### Dockerization:
- Dockerize the Django application.
- Ensure that the application runs in a container without errors.

## Submission Guidelines:

### Code Submission:
- Submit the Django project as a compressed file or provide a link to a version control repository (GitHub, GitLab, etc.).
- Include the Dockerfile for containerization.
- Clearly document any additional setup or configuration required.

### Documentation:
- Provide a brief documentation file explaining how to run the application and access the API endpoints.

### Testing:
- Include a set of sample API requests to demonstrate the functionality of the created API endpoints.
- Ensure that the API authentication is working as expected.

## Additional Notes:
- Follow best practices for Django and DRF development.
- Use Git for version control if possible.
- Feel free to use any additional Django or Python packages that you find necessary.
