from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import json

app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(days=5)

db = SQLAlchemy(app)


class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    chosen_courses = db.Column(db.Text, default="[]")  # Default is valid JSON
    marks = db.Column(db.Text, default="{}")  # Default is valid JSON
    weights = db.Column(db.Text, default="{}")  # Default is valid JSON

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.chosen_courses = "[]"  # Initialize as valid JSON
        self.marks = "{}"  # Initialize as valid JSON
        self.weights = "{}"  # Initialize as valid JSON




@app.route("/home", methods=["POST", "GET"])
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        email = request.form["email"]
        
        if not user or not email:
            flash("Invalid input. Please enter both name and email.", "warning")
            return redirect(url_for("home"))
        
        session["user"] = user


        found_user = users.query.filter_by(name=user).first() #major security risk, u log in based on name only, no double checking

        if found_user:
            # Load chosen courses, marks, and weights from the database
            try:
                session["chosen_courses"] = json.loads(found_user.chosen_courses)
            except json.JSONDecodeError:
                session["chosen_courses"] = []

            try:
                session["marks"] = json.loads(found_user.marks)
            except json.JSONDecodeError:
                session["marks"] = {}

            try:
                session["weights"] = json.loads(found_user.weights)
            except json.JSONDecodeError:
                session["weights"] = {}
        else:
            # Create a new user with default values
            usr = users(user, email)
            db.session.add(usr)
            db.session.commit()

            # Initialize session data for new users
            session["chosen_courses"] = []
            session["marks"] = {}
            session["weights"] = {}

        flash(f"You are logged in! {user}", "info")
        return redirect(url_for("catalogue"))
    else:
        if "user" in session:
            flash(f"You are already logged in! {session['user']}", "info")
            return redirect(url_for("catalogue"))
        return render_template("home.html")


@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())


@app.route("/add_course", methods=['POST'])
def add_course():
    if "user" not in session:
        return jsonify({"success": False, "error": "Not logged in"}), 401

    course_name = request.json.get('course')

    user = users.query.filter_by(name=session["user"]).first()
    chosen_courses = json.loads(user.chosen_courses)

    if course_name not in chosen_courses:
        chosen_courses.append(course_name)
        user.chosen_courses = json.dumps(chosen_courses)
        db.session.commit()

        # Update the session
        session["chosen_courses"] = chosen_courses
        total_units = calculate_total_units(chosen_courses)
    return jsonify({"success": True, "chosen_courses": chosen_courses, "total_units": total_units})

@app.route("/remove_course", methods=['POST'])
def remove_course():
    if "user" not in session:
        return jsonify({"success": False, "error": "Not logged in"}), 401

    course_name = request.json.get('course')

    user = users.query.filter_by(name=session["user"]).first()
    chosen_courses = json.loads(user.chosen_courses)

    chosen_courses = [course for course in chosen_courses if course != course_name]
    user.chosen_courses = json.dumps(chosen_courses)
    db.session.commit()

    # Update the session
    session["chosen_courses"] = chosen_courses
    total_units = calculate_total_units(chosen_courses)
    return jsonify({"success": True, "chosen_courses": chosen_courses, "total_units": total_units})

def calculate_total_units(chosen_courses):
    total = 0
    for course in chosen_courses:
        if "Extension" in course:
            total += 1
        else:
            total += 2
    return total


@app.route("/catalogue")
def catalogue():
    if "user" in session:
        with sqlite3.connect("instance/database_course.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM courses")
            courses = cursor.fetchall()

        # Use the session's chosen_courses
        chosen_courses = session.get("chosen_courses", [])
        total_units = calculate_total_units(chosen_courses)
        return render_template("catalogue.html", courses=courses, chosen_courses=chosen_courses, total_units=total_units)

    flash("You need to log in!", "info")
    return redirect(url_for("home"))


@app.route("/marks")
def marks():
    if "user" in session:
        user = users.query.filter_by(name=session["user"]).first()

        if not user:
            flash("User not found!", "error")
            return redirect(url_for("home"))

        # Load marks and weights from the database
        try:
            marks = json.loads(user.marks)
            weights = json.loads(user.weights)
        except json.JSONDecodeError:
            marks = {}
            weights = {}
        chosen_courses = session.get("chosen_courses", [])
        total_units = calculate_total_units(chosen_courses)
        return render_template("marks.html", chosen_courses=chosen_courses, total_units=total_units, marks=marks, weights=weights)
    
    flash("You need to log in!", "info")
    return redirect(url_for("home"))

@app.route("/save_marks", methods=["POST"])
def save_marks():
    if "user" not in session:
        return jsonify({"success": False, "error": "Not logged in"}), 401

    data = request.json
    user = users.query.filter_by(name=session["user"]).first()

    if not user:
        return jsonify({"success": False, "error": "User not found"}), 404

    # Ensure data is valid before saving
    try:
        marks = data.get("marks", {})
        weights = data.get("weights", {})

        # Update the database
        user.marks = json.dumps(marks)
        user.weights = json.dumps(weights)
        db.session.commit()

        # Update the session
        session["marks"] = marks
        session["weights"] = weights

        return jsonify({"success": True, "marks": marks, "weights": weights})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400


@app.route("/subject")
def subject():
    if "user" in session: 
        with sqlite3.connect("instance/database_course.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM courses")
            courses = cursor.fetchall()
        return render_template("subject.html", courses=courses)
    else:
        flash("You need to log in!", "info")
        return redirect(url_for("home"))

@app.route("/get_course_info/<course_name>")
def get_course_info(course_name):
    # Connect to the database to fetch course info
    with sqlite3.connect("instance/database_course_info.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT description, difficulty, scaling FROM courses_extended WHERE course=?", (course_name,))
        course_info = cursor.fetchone()

    if course_info:
        # Return the course info as a JSON response
        return jsonify({
            "description": course_info[0],
            "difficulty": course_info[1],
            "scaling": course_info[2]
        })
    else:
        # Return a default response if course not found
        return jsonify({
            "description": "No description available.",
            "difficulty": "No difficulty information available.",
            "scaling": "No scaling information available."
        })


@app.route("/logout")
def logout():
    if "user" in session: 
        user = session["user"]
        flash(f"You have been logged out! {user}", "info")
    session.pop("user", None)
    session.pop("email", None)
    session.pop("courses", None)
    session.pop("marks", None)
    session.pop("weights", None)


    return redirect(url_for("home"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)