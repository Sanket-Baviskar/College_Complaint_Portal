# College Complaint Portal (Django)

A mini-project to submit, route, and track complaints to college departments.

## Quick Start

```bash
# 1) Create & activate a virtual environment (Windows PowerShell)
python -m venv env
env\Scripts\activate

# or on Linux/macOS
python -m venv env
source env/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Migrate database & create superuser
python manage.py migrate
python manage.py createsuperuser  # create admin/staff account

# 4) Load seed departments
python manage.py loaddata portal/fixtures/seed_departments.json

# 5) Run server
python manage.py runserver
```

## Log in

- Admin: visit `/admin/` to manage Departments and view Complaints.
- Students: visit `/login/` to sign in (use admin to create student users or `createsuperuser` for testing).

## Staff Tip (Department Mapping)

For each staff user, set their **First name** to match the Department name (e.g., `Computer Engineering`).
Dashboard will auto-filter by that department by default. You can also filter via the dropdown.

## Features
- Submit complaints with department, priority, and optional attachment
- Student view to track their complaints
- Staff dashboard with status update form
- Admin management in Django Admin

## Notes
- Uses SQLite (db.sqlite3 created on first migrate).
- Attachments will be stored in `MEDIA_ROOT` if you add MEDIA settings; otherwise uploaded files work in development.
- For production, configure ALLOWED_HOSTS, DEBUG, STATIC, and MEDIA properlyssdfsd.
 
