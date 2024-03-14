from flask import Flask, render_template, redirect, request,url_for
from database import *
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route("/users")
def students():
   user = fetch_data("users")
   print(user)
   return render_template("students.html", user = user)



@app.route("/register")
def register():
   return render_template("register.html")

@app.route('/courses')
def courses():
    course = fetch_data("courses")
    return render_template("courses.html", course=course)


@app.route('/adduser', methods=["POST", "GET"])
def signup():
   if request.method=="POST":
      fullname = request.form["fullname"]
      email = request.form["email"]
      phone = request.form["phone"]
      password = request.form["password"]
      address = request.form["address"]
      h_password = generate_password_hash(password)
      user=(fullname,email,phone,address,h_password,'now()')
      add_user(user)
   return redirect("/register")

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        users = fetch_data('users')
        for user in users:
            dbemail = user[2]
            dbpass = user[5]
            if dbemail == email and check_password_hash(dbpass, password):
                # Redirect to dashboard or homepage after successful login
                return redirect(redirect('/'))  # Assuming you have a route named 'dashboard'
    return redirect('/login')


if __name__ == '__main__':

    app.run(debug=True)
    