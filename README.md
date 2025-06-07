# Portfolio WebSite

This is a personal portfolio project built with Django. It allows you to manage projects, tags, contacts, and features a custom admin area.

## Features

- Project listing and detail pages
- Tag filtering
- Custom admin area for managing projects, tags, and received emails
- Contact form with validation and email sending
- Image upload for projects and tags

## Project Structure

```
admin_app/         # Custom admin app
main_app/          # Main app (home, about, contact)
projects_app/      # Projects app
base_static/       # Global static files (CSS, JS, images)
base_templates/    # Base templates and global partials
media/             # Image uploads
utils/             # Utility scripts
manage.py          # Django management script
requirements.txt   # Project dependencies
.env-example       # Example environment variables
```

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Felipe-Gibin/Portifolio-WebSite.git
   cd Portifolio-WebSite
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   - Copy `.env-example` to `.env` and fill in the required values.

5. Run migrations:
   ```sh
   python manage.py migrate
   ```

6. Start the server:
   ```sh
   python manage.py runserver
   ```

## Useful Scripts

- Run all migrations automatically:
  ```sh
  sh utils/migrations.sh
  ```

## License

Distributed under the [GNU GPL v3](LICENSE).

---