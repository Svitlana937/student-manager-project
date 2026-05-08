from flask import Flask, render_template
import studentDAO

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    students = studentDAO.get_all_students()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

