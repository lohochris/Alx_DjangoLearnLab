## Custom Permissions and Groups

This project includes custom permissions for the `Book` model:
- `can_publish_books`: Allows users to publish books.
- `can_archive_books`: Allows users to archive books.

### How to Use
- Superusers automatically have all permissions.
- Other users need to be added to the `Publisher` group to gain publishing rights.

### Assigning Permissions
You can assign users to the `Publisher` group via the Django Admin interface.
