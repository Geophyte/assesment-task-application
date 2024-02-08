def generate_data(num_records=10):
    fake = Faker()
    User = get_user_model()

    # Generate categories
    categories = ['Work', 'Personal', 'Shopping', 'Health', 'Education']
    Category.objects.bulk_create([Category(name=name) for name in categories])

    # Generate tasks
    for _ in range(num_records):
        title = fake.text(max_nb_chars=50)
        description = fake.text(max_nb_chars=200)
        completed = random.choice([True, False])
        category = random.choice(Category.objects.all())
        Task.objects.create(title=title, description=description, completed=completed, category=category)

    # Generate users
    for _ in range(num_records):
        username = fake.user_name()
        email = fake.email()
        password = fake.password()
        bio = fake.text(max_nb_chars=200)
        profile_picture = None
        CustomUser.objects.create(username=username, email=email, password=password, bio=bio, profile_picture=profile_picture)

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
    from django.contrib.auth.models import User
    from api.models import Category, Task, CustomUser, Comment
    from django.contrib.auth import get_user_model

    num_records = 10
    generate_data(num_records)
