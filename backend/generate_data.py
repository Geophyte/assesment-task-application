def generate_data(num_records=10):
    fake = Faker()

    # Generate users
    for _ in range(num_records):
        username = fake.user_name()
        email = fake.email()
        password = fake.password()
        bio = fake.text(max_nb_chars=200)
        profile_picture = None
        CustomUser.objects.create(username=username, email=email, password=password, bio=bio, profile_picture=profile_picture)

    # Generate categories
    categories = ['Work', 'Personal', 'Shopping', 'Health', 'Education']
    for name in categories:
        created_by = random.choice(CustomUser.objects.all())
        existing_category = Category.objects.filter(name=name).exists()
        if not existing_category:
            Category.objects.create(name=name, created_by=created_by)

    # Generate tasks
    for _ in range(num_records):
        title = fake.text(max_nb_chars=50)
        description = fake.text(max_nb_chars=200)
        completed = random.choice([True, False])
        category = random.choice(Category.objects.all())
        created_by = random.choice(CustomUser.objects.all())
        last_modified_by = random.choice(CustomUser.objects.all())
        Task.objects.create(title=title, description=description, completed=completed, category=category, created_by=created_by, last_modified_by=last_modified_by)

    # Generate comments
    for _ in range(num_records):
        task = random.choice(Task.objects.all())
        user = random.choice(CustomUser.objects.all())
        text = fake.text(max_nb_chars=100)
        Comment.objects.create(task=task, user=user, text=text)


if __name__ == '__main__':
    import os
    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    application = get_wsgi_application()

    import random
    from faker import Faker
    from api.models import Category, Task, CustomUser, Comment

    num_records = 10
    generate_data(num_records)
