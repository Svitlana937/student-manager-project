from flask import Flask, render_template
import studentDAO
from flask import jsonify

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    students = studentDAO.get_all_students()
    return render_template("index.html", students=students)

def get_student(student_id):
    student = studentDAO.get_student_by_id(student_id)
    return render_template("student.html", student=student)

@app.route("/student/<int:student_id>", methods=["GET"])
def get_student_id(student_id):
    student = studentDAO.get_student_by_id(student_id)
    if student:
        return jsonify(student)
    else:
        return jsonify({"error": "Student not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)

