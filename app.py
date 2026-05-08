from flask import Flask, render_template
import studentDAO

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    students = studentDAO.get_all_students()
    return render_template("index.html")

def get_student(student_id):
    student = studentDAO.get_student_by_id(student_id)
    return render_template("student.html", student=student)


if __name__ == "__main__":
    app.run(debug=True)

