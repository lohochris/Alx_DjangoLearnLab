# relationship_app/scripts/create_groups.py
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from relationship_app.models import Book

class Command(BaseCommand):
    help = 'Create default groups and assign permissions'

    def handle(self, *args, **kwargs):
        # Define groups and permissions
        groups_permissions = {
            'Admins': ['can_add_book', 'can_change_book', 'can_delete_book'],
            'Editors': ['can_add_book', 'can_change_book'],
            'Viewers': []
        }

        # Get Content Type for Book model
        book_content_type = ContentType.objects.get_for_model(Book)

        # Loop through groups and assign permissions
        for group_name, perms in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm in perms:
                permission = Permission.objects.get(codename=perm, content_type=book_content_type)
                group.permissions.add(permission)
            self.stdout.write(self.style.SUCCESS(f'Permissions assigned to {group_name}'))
