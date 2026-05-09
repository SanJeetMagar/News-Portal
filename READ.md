# News Portal Backend

A Django REST Framework backend for a news portal application. The project provides APIs for user authentication, authors, articles, categories, media uploads, ads, comments, reactions, and basic analytics tracking.

## Tech Stack

- Python
- Django 5.2.6
- Django REST Framework
- Simple JWT authentication
- SQLite for local development
- drf-spectacular for OpenAPI schema and Swagger docs
- django-filter
- django-cors-headers
- Pillow for image uploads

## Project Structure

```text
news-portal-backend/
|-- manage.py
|-- requirements.txt
|-- db.sqlite3
|-- src/
|   |-- settings.py
|   |-- urls.py
|   `-- apps/
|       |-- auth/
|       |-- authors/
|       |-- articles/
|       |-- categories/
|       |-- interactions/
|       |-- news_media/
|       |-- ads/
|       |-- analytics/
|       `-- common/
`-- READ.md
```

## Main Features

- Custom user model with role support
- User registration, login, logout, and profile update
- JWT access and refresh token authentication
- Author profiles linked to users
- Article listing, detail view, and author-managed article creation
- Category CRUD with automatic slug generation
- Comments, threaded replies, and reactions
- Media upload API for images, videos, audio, and documents
- Advertisement management with placements, categories, advertiser ownership, and active date filtering
- Article view tracking and category click tracking
- Swagger, ReDoc, and OpenAPI schema generation in debug mode

## User Roles

The project defines these roles:

- `superadmin`
- `admin`
- `advertiser`
- `editor`
- `author`
- `user`

Role-based permissions are implemented in `src/apps/common/permissions.py`.

## Setup

### 1. Clone the project

```bash
git clone <repository-url>
cd news-portal-backend
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

An example environment file is available at `.env.example`.

```bash
cp .env.example .env
```

The current settings file uses SQLite by default. JWT token lifetimes can be configured with:

```env
ACCESS_TOKEN_LIFETIME=60
REFRESH_TOKEN_LIFETIME=7
```

If these values are not set, the project defaults to:

- Access token lifetime: 60 minutes
- Refresh token lifetime: 7 days

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

The custom user model uses email as the login field.

### 7. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## API Documentation

When `DEBUG=True`, API documentation is available at:

| URL | Description |
| --- | --- |
| `/` | Swagger UI |
| `/schema/` | OpenAPI schema |
| `/redoc/` | ReDoc documentation |
| `/admin/` | Django admin |

## Authentication

Authentication uses JWT bearer tokens.

### Register

```http
POST /api/v1/auth/register/
```

Example body:

```json
{
  "first_name": "Sanjeet",
  "last_name": "Magar",
  "username": "sanjeet",
  "email": "sanjeet@example.com",
  "password": "strong-password",
  "role": "user",
  "phone": "9800000000"
}
```

### Login

```http
POST /api/v1/auth/login/
```

Example body:

```json
{
  "email": "sanjeet@example.com",
  "password": "strong-password"
}
```

Successful login returns:

```json
{
  "msg": "Login successful",
  "refresh": "<refresh-token>",
  "access": "<access-token>",
  "details": {
    "id": "<user-id>",
    "first_name": "Sanjeet",
    "last_name": "Magar",
    "username": "sanjeet",
    "email": "sanjeet@example.com",
    "role": "user",
    "phone": "9800000000"
  }
}
```

### Authenticated Requests

Send the access token in the `Authorization` header:

```http
Authorization: Bearer <access-token>
```

### Logout

```http
POST /api/v1/auth/logout/
```

Example body:

```json
{
  "refresh": "<refresh-token>"
}
```

### Profile

```http
GET /api/v1/auth/profile/
PUT /api/v1/auth/profile/
PATCH /api/v1/auth/profile/
```

Requires authentication.

## API Endpoints

All versioned API routes are mounted under:

```text
/api/v1/
```

### Auth

| Method | Endpoint | Description |
| --- | --- | --- |
| `POST` | `/api/v1/auth/register/` | Register a new user |
| `POST` | `/api/v1/auth/login/` | Login and receive JWT tokens |
| `POST` | `/api/v1/auth/logout/` | Blacklist a refresh token |
| `GET` | `/api/v1/auth/profile/` | Get logged-in user profile |
| `PUT/PATCH` | `/api/v1/auth/profile/` | Update logged-in user profile |

### Articles

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/v1/articles/` | List published articles |
| `GET` | `/api/v1/articles/<int:pk>/` | Retrieve an article detail route currently declared in URLs |
| `GET` | `/api/v1/articles/author/` | List articles for the logged-in author |
| `POST` | `/api/v1/articles/author/` | Create an article as the logged-in author |
| `GET` | `/api/v1/articles/author/<slug:slug>/` | Retrieve an author's article |
| `PUT/PATCH/DELETE` | `/api/v1/articles/author/<slug:slug>/` | Update or delete an author's article |

### Authors

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/v1/authors/` | List authors |
| `GET` | `/api/v1/authors/<slug:slug>/` | Retrieve an author profile |
| `GET` | `/api/v1/authors/me/update/` | Get logged-in author's profile |
| `PUT/PATCH` | `/api/v1/authors/me/update/` | Update logged-in author's profile |

### Categories

The categories app is mounted at `/api/v1/categories/` and currently defines routes with an additional `categories/` prefix.

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/v1/categories/categories/` | List categories |
| `POST` | `/api/v1/categories/categories/` | Create a category |
| `GET` | `/api/v1/categories/categories/<slug:slug>/` | Retrieve a category and track a click |
| `PUT/PATCH/DELETE` | `/api/v1/categories/categories/<slug:slug>/` | Update or delete a category |

### Interactions

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/v1/interactions/comments/` | List comments |
| `POST` | `/api/v1/interactions/comments/` | Create a comment |
| `GET` | `/api/v1/interactions/comments/<int:pk>/` | Retrieve a comment |
| `PUT/PATCH/DELETE` | `/api/v1/interactions/comments/<int:pk>/` | Update or delete a comment |
| `GET` | `/api/v1/interactions/reactions/` | List article reactions |
| `POST` | `/api/v1/interactions/reactions/` | React to an article |

### Media

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/v1/news_media/media/` | List media files |
| `POST` | `/api/v1/news_media/media/` | Upload a media file |
| `GET` | `/api/v1/news_media/media/<pk>/` | Retrieve a media file |
| `PUT/PATCH/DELETE` | `/api/v1/news_media/media/<pk>/` | Update or delete a media file |

### Ads

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/api/v1/ads/` | List currently active ads |
| `POST` | `/api/v1/ads/create/` | Create an ad as an admin, superadmin, or advertiser |
| `GET` | `/api/v1/ads/<slug:slug>/` | Retrieve an ad |
| `PUT/PATCH/DELETE` | `/api/v1/ads/<slug:slug>/` | Update or delete an ad as owner or admin |

Ad list filters:

```text
/api/v1/ads/?placement=sidebar
/api/v1/ads/?category=<category-id>
```

Available ad placements:

- `homepage`
- `sidebar`
- `article_top`
- `article_middle`
- `article_bottom`
- `popup`

## Core Models

### User

Custom authentication model with:

- email login
- first name and last name
- username
- phone
- role
- profile image
- address
- email verification flag

### Author

Author profile linked one-to-one with a user. Includes:

- name
- slug
- bio
- profile image
- designation
- social links

### Article

News article model with:

- title
- slug
- content
- excerpt
- authors
- category
- status: `draft` or `published`
- feature image

### Category

Category model with:

- name
- slug
- timestamps

### Comment

Comment model with:

- user
- article
- optional parent comment for replies
- content
- approval status

### Reaction

Article and comment reactions support:

- `happy`
- `sad`
- `angry`
- `love`
- `surprised`

### Ad

Advertisement model with:

- title
- slug
- image
- link
- type: `general` or `category`
- placement
- optional category
- advertiser
- active status
- start and end dates

## Development Commands

Run Django system checks:

```bash
python manage.py check
```

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Run tests:

```bash
python manage.py test
```

Open Django shell:

```bash
python manage.py shell
```

## Notes

- `READ.md` is the current project documentation file. Many projects use `README.md`, so renaming may be useful later if the repository is published.
- The project includes `src/apps/analytics/urls.py`, but analytics routes are not currently mounted in `src/urls.py`.
- `ArticleDetailView` uses slug lookup, while the current article detail URL is declared as `<int:pk>`. Change that URL to `<slug:slug>` if article detail should be accessed by slug.
- Models use UUID primary keys through `TimestampModel`, but a few routes are currently declared with `<int:pk>`.
- The settings file is configured for local development with SQLite, `DEBUG=True`, and open CORS. Update these settings before production deployment.

## License

No license file is currently included in this repository.
