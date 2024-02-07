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
