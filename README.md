# CRUD_Ops – Django CRUD Project for Teachers, Students & Classes

This is a simple Django web application that demonstrates CRUD (Create, Read, Update, Delete) operations for managing **teachers**, **students**, and **classes**. 
The project uses **function-based views** and includes custom models, forms, templates, and admin configuration.

---

##Features

- Add, edit, and delete **teachers**
- Add, edit, and delete **students**
- Join students to classes
- View lists of all teachers, students, and classes
- Basic navigation with reusable templates
- Admin panel for managing all models

---

## Tech Stack

- **Python 3**
- **Django**
- **SQLite** (default Django database)
- **HTML/CSS (Templates)**
- **Django Admin**
- **Function-Based Views (FBV)**

---

## 📁 Project Structure

```

CRUD\_Ops/
│
├── myapp/                    # Main Django app
│   ├── migrations/
│   ├── **pycache**/
│   ├── admin.py              # Admin config
│   ├── apps.py
│   ├── form.py               # Custom Django forms
│   ├── models.py             # Models for Teacher, Student, Class
│   ├── views.py              # Function-based views
│   └── tests.py
│
├── static/images/            # Static image assets
│   └── img.jpg
│
├── templates/                # HTML templates
│   ├── addteacher.html
│   ├── base.html
│   ├── classlist.html
│   ├── editteacher.html
│   ├── joinclass.html
│   ├── stu\_add.html
│   ├── stu\_list.html
│   └── teacherlist.html
│
├── db.sqlite3                # SQLite database
├── manage.py                 # Django management script
└── README.md

````

---

## ⚙️ How to Run This Project

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/CRUD_Ops.git
cd CRUD_Ops
````

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Now open your browser and go to:
`http://127.0.0.1:8000/` – Main site
`http://127.0.0.1:8000/admin/` – Admin panel

---

## 🧩 Notes

* Admin panel can be used to add teachers, students, and classes manually.
* All CRUD operations are implemented using Django's **function-based views**, not class-based views.
* Templates are styled minimally and structured using a common `base.html`.
* Static files like images are stored under the `static/` folder.

---

## 📌 Future Improvements

* Add pagination and search for student/teacher lists
* Add class schedules or subjects
* Switch to Class-Based Views (CBV) for scalability
* Implement user authentication for different roles (admin, teacher, student)

