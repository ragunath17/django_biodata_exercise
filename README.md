# BioData REST API (Django REST Framework)

## Overview
This project is a BioData management API built using Django REST Framework.

It demonstrates:
- Function Based Views
- Class Based Views (APIView)
- JWT Authentication
- Pagination
- Filtering (django-filter)
- PUT and PATCH update methods
- Unique field validation

---

## Installation

1. Clone the repository

2. Create virtual environment
   python -m venv venv

3. Activate virtual environment

4. Install dependencies
   pip install -r requirements.txt

5. Run migrations
   python manage.py migrate

6. Run server
   python manage.py runserver

---

## API Endpoints

Function Based Views:
- /biodata/list/
- /biodata/<id>/

Class Based Views:
- /biodata/cbv/list/
- /biodata/cbv/<id>/

---

## Features Implemented

- CRUD operations
- Pagination
- Filtering by first_name, last_name, job_title, email, city
- Serializer validation
- Partial update (PATCH)
