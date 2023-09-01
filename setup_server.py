import os
import sys
import django
from django.core.management import execute_from_command_line

# Set the Django settings module (change 'your_project' to your actual project name)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todolist.settings")

# Initialize Django
django.setup()


def main():
    # Run database migrations
    print("Running database migrations...")
    execute_from_command_line(["manage.py", "migrate"])

    # Create a superuser
    create_superuser = input("Create a superuser? (yes/no): ").strip().lower()
    if create_superuser == "yes":
        execute_from_command_line(["manage.py", "createsuperuser"])

    # Start the Django development server
    execute_from_command_line(["manage.py", "runserver"])


if __name__ == "__main__":
    main()
