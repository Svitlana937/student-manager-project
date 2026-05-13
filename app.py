from flask import Flask, render_template, request, url_for, redirect, jsonify, session
import studentDAO
# Reference: Flask session handling
# https://runestone.academy/ns/books/published/webfundamentals/Flask/sessions.html
from flask_session import Session

# Reference: Create quick Flask app
# https://flask.palletsprojects.com/en/2.3.x/quickstart/
app = Flask(__name__)

# Authentication
# Reference: 
#https://www.geeksforgeeks.org/python/how-to-use-flask-session-in-python-flask/

                   # Configuration 
app.config["SESSION_PERMANENT"] = False     # Sessions expire when the browser is closed
app.config["SESSION_TYPE"] = "filesystem"     # Store session data in files

# # Need key to avoid error: "RuntimeError: The session is unavailable because no secret key was set
app.config["SECRET_KEY"] = "secret_key" 

# Initialize Flask-Session
Session(app)

# Defining Routes for Session Handling
# Reference: Flask session handling
# https://www.geeksforgeeks.org/python/how-to-use-flask-session-in-python-flask/
@app.route("/")
def index():
    # If no username in session, redirect to login
    if not session.get("name"):
        return render_template("login.html")

    students = studentDAO.get_all_students()
    return render_template("index.html", students=students, username=session.get("name"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("name")
        password = request.form.get("password")

        user = studentDAO.check_user(username, password)
        if user:
            # Record the user name in session
            session["name"] = username
            return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    # Clear the username from session
    session["name"] = None
    return redirect(url_for("login"))



#------- ROUTES --------
# Reference: Flask routing 
# https://flask.palletsprojects.com/en/stable/quickstart/#routing

# Route to add student
@app.route("/add_student", methods=["POST"])
def add_student():
    if request.is_json:
        data = request.get_json()
        name = data.get("name")
        age = data.get("age")
    else:
        name = request.form.get("name")
        age = request.form.get("age")

    studentDAO.add_student(name, age)

    if not request.is_json:
        return redirect(url_for("index"))

    new_student = studentDAO.add_student(name, age)
    return jsonify({"message": "Student added successfully", "student": new_student})

# PUT route to update student information
@app.route("/api/update_student/<int:student_id>", methods=["PUT"])
def update_student_api(student_id):
    data = request.get_json()
    name = data.get("name")
    age = data.get("age")

    studentDAO.update_student(student_id, name, age)
    return jsonify({"message": "Student updated successfully"})

    
def get_student(student_id):
    student = studentDAO.get_student_by_id(student_id)
    return render_template("student.html", student=student)


@app.route("/student/<int:student_id>")
def get_student_id(student_id):
    student = studentDAO.get_student_by_id(student_id)
    if student:
        return render_template("student.html", student=student)
    else:
        return render_template("student_not_found.html")



@app.route("/delete_student/<int:student_id>")
def delete_student(student_id):
    studentDAO.delete_student(student_id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

