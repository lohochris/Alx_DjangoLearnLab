#  Advanced API Project

## API Endpoints
| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/books/` | GET | Retrieve all books |  No |
| `/books/<id>/` | GET | Retrieve a single book by ID |  No |
| `/books/create/` | POST | Add a new book |  Yes |
| `/books/update/<id>/` | PUT/PATCH | Update a book |  Yes |
| `/books/delete/<id>/` | DELETE | Remove a book |  Yes |

## 🛠 Setup & Run
1. Install dependencies:
   ```sh
   pip install django djangorestframework
