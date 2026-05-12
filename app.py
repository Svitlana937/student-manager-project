from flask import Flask, render_template, request, url_for, redirect
import studentDAO
from flask import jsonify
import studentDAO

app = Flask(__name__)

@app.route("/")
def index():
    students = studentDAO.get_all_students()
    return render_template("index.html", students=students)

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


@app.route("/add_student", methods=["POST"])
def add_student():
    name = request.form.get("name")
    age = request.form.get("age")

    if name and age:
        studentDAO.add_student(name, age)
        return redirect("/")
        
    return "Name and age are required"
    

@app.route("/delete_student/<int:student_id>")
def delete_student(student_id):
    studentDAO.delete_student(student_id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

