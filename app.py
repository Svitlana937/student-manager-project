from flask import Flask, render_template, request, url_for, redirect, jsonify
import studentDAO


# Reference: Create quick Flask app
# https://flask.palletsprojects.com/en/2.3.x/quickstart/
app = Flask(__name__)


#------- ROUTES --------
# Reference: Flask routing 
# https://flask.palletsprojects.com/en/stable/quickstart/#routing

# Main page route
@app.route("/")
def index():
    students = studentDAO.get_all_students()
    return render_template("index.html", students=students)

# POST route to add a new student
@app.route("/api/add_student", methods=["POST"])
def add_student_api():
    data = request.get_json()
    name = data.get("name")
    age = data.get("age")

    new_student = studentDAO.add_student(name, age)
    return jsonify({"message": "Student added successfully", "student": new_student})

# Form to add student
@app.route("/add_student", methods=["POST"])
def add_student():
    name = request.form.get("name")
    age = request.form.get("age")

    studentDAO = studentDAO.StudentDAO()

    return "Name and age are required"

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

