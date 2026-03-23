# BioData Management System (Django + DRF)

## Overview
This project is a BioData Management System built using Django and Django REST Framework.

It supports both REST APIs and server-side rendering using Django Templates to manage and display biodata records.

---

## Features

### Backend (Django REST Framework)
- Function-Based Views (FBV)
- Class-Based Views (APIView)
- Generic Views
- CRUD operations (Create, Read, Update, Delete)
- Filtering (first_name, last_name, job_title, email, city)
- Serializer validation
- PUT and PATCH support

### Frontend (Django Templates)
- List view to display all records
- Detail view for individual biodata
- Form handling for Create and Update
- Dynamic data rendering

---

## Tech Stack
- Python
- Django
- Django REST Framework
- MySQL
- HTML (Django Templates)

---

## Project Structure
bio_data/
│
├── api/
│ ├── serializers.py
│ ├── views.py
│ ├── cbv_views.py
│ ├── generic_views.py
│ ├── paginations.py
│ ├── filters.py
│ └── urls.py
│
├── templates/
│ ├── biodata_detail.html
│ ├── biodata_form.html
│ └── data.html
│
├── models.py
├── views.py
├── urls.py
└── migrations/

---

## How to Run

1. Create virtual environment  
   python -m venv venv  

2. Activate environment  
   venv\Scripts\activate  

3. Install dependencies  
   pip install -r requirements.txt  

4. Apply migrations  
   python manage.py migrate  

5. Run server  
   python manage.py runserver  

---

## API Endpoints

### Function-Based Views
- /biodata/list/
- /biodata/<id>/

### Class-Based Views
- /biodata/cbv/list/
- /biodata/cbv/<id>/

---

## Template Pages

- /biodata/ → List Page  
- /biodata/<id>/ → Detail Page  
- Form page for Create and Update  

---

## Key Learnings
- Working with FBV, APIView, and Generic Views
- Building CRUD operations using both API and Templates
- Handling forms and template rendering
- Implementing filtering and validations

---

## Future Improvements
- Add authentication (JWT / login system)
- Improve UI with CSS or Bootstrap
- Enable pagination in UI
- Deploy the project

