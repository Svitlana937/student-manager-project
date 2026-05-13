# Student Manager Project

A web-based student management system built with Flask and MySQL that allows users to authenticate, view, add, edit, and delete student records.

## Overview

This application provides a simple yet functional interface for managing student information. Users must authenticate with credentials before accessing the student directory. The system uses Flask for the web framework, MySQL for data persistence, and Flask-Session for session management.

## Features

- **User Authentication**: Simple login system with session management
- **Session-based Access Control**: Secure session handling using filesystem storage
- **CRUD Operations**: Create, Read, Update, and Delete student records
- **Responsive UI**: Bootstrap-based responsive design
- **RESTful API Support**: Dual support for form-based and JSON requests
- **Database Integration**: MySQL database connectivity with proper connection handling

## Technologies Used

- **Backend**: Flask 2.3.x
- **Database**: MySQL with `mysql-connector-python`
- **Frontend**: Bootstrap 4.1.3 (CDN), HTML5
- **Session Management**: Flask-Session with filesystem storage
- **Server**: Python 3

## Installation

### Prerequisites

- Python 3.6+
- MySQL Server installed and running
- pip package manager

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd student-manager-project
   ```

2. **Create virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install Flask flask-session mysql-connector-python
   ```

4. **Configure database connection**
   - Edit `db_config.py` and update MySQL credentials:
     ```python
     mysql.connector.connect(
         host="localhost",
         user="your_username",
         password="your_password",
         database="your_database"
     )
     ```

5. **Initialize database**
   ```bash
   python init_db.py
   ```

## Running the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

**Default Login Credentials**:
- Username: `root`
- Password: `pass`

## Project Structure

```
student-manager-project/
├── app.py                 # Main Flask application with routes
├── db_config.py          # Database connection configuration
├── studentDAO.py         # Data Access Object for student operations
├── init_db.py            # Database initialization script
├── insert_db.py          # Script to insert sample data
├── update_db.py          # Database update utilities
├── delete_db.py          # Database cleanup script
├── view_db.py            # Database viewing utilities
├── requirements.txt      # Python dependencies
├── static/
│   └── style.css         # Custom stylesheet
├── templates/
│   ├── index.html        # Main student directory view
│   ├── login.html        # Login page
│   └── edit_student.html # Student edit form
└── flask_session/        # Session storage directory
```

## Key Files Description

- **app.py**: Contains all Flask routes including:
  - `/` - Dashboard (requires authentication)
  - `/login` - Login endpoint
  - `/logout` - Logout endpoint
  - `/add_student` - Add new student
  - `/edit_student/<id>` - Edit student form
  - `/update_student_api/<id>` - Update student (supports both form and JSON)
  - `/delete_student/<id>` - Delete student

- **studentDAO.py**: Data Access Object pattern implementation with methods:
  - `get_all_students()` - Retrieve all students
  - `get_student_by_id(id)` - Retrieve specific student
  - `add_student(name, age)` - Insert new student
  - `update_student(id, name, age)` - Update student record
  - `delete_student(id)` - Delete student record
  - `check_user(username, password)` - User authentication

## API Endpoints

### Authentication
- **POST** `/login` - User login with session creation
- **GET** `/logout` - Clear session and redirect to login

### Students
- **GET** `/` - View all students (requires authentication)
- **POST** `/add_student` - Add new student
- **GET** `/edit_student/<id>` - Display edit form
- **POST/PUT** `/update_student_api/<id>` - Update student (form or JSON)
- **GET** `/delete_student/<id>` - Delete student

## References

All references used in this code are documented below with their exact purpose:

### Flask Framework
- **Flask Quickstart**: https://flask.palletsprojects.com/en/2.3.x/quickstart/
  - Used for: Basic Flask application setup, configuration, and app initialization
  
- **Flask Routing**: https://flask.palletsprojects.com/en/stable/quickstart/#routing
  - Used for: Route definitions with `@app.route()` decorator, HTTP methods (GET, POST, PUT)

- **Flask Session Handling**: https://www.geeksforgeeks.org/python/how-to-use-flask-session-in-python-flask/
  - Used for: Session configuration, session data storage, `session.get()` operations

- **Flask-Session Documentation**: https://runestone.academy/ns/books/published/webfundamentals/Flask/sessions.html
  - Used for: Flask-Session integration, filesystem-based session storage, session initialization

### Frontend
- **Bootstrap 4.1.3 CSS Framework**: https://getbootstrap.com/
  - Used for: Responsive grid layout, form styling, button components, card components, spacing utilities (Bootstrap CDN: `https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css`)

### Database
- **MySQL Connector for Python**: https://dev.mysql.com/doc/connector-python/en/
  - Used for: `mysql.connector.connect()`, cursor operations, SQL query execution, database connection management

### Software Patterns
- **Data Access Object (DAO) Pattern**: https://en.wikipedia.org/wiki/Data_access_object
  - Used for: Separating database logic in `studentDAO.py`, abstracting CRUD operations

---

**Author**: Student Manager Project  
**License**: MIT  
**Last Updated**: 2026