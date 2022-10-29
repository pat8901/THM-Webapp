
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    return render_template("login.html",text="Hello World!")
=======
=======
>>>>>>> Stashed changes
    data = request.form
    print(data)
    return render_template("login.html")
>>>>>>> Stashed changes

@auth.route("/logout")
def logout():
    return render_template("logout.html")

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('Name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 5:
            flash('Password must be longer than 4 characters.', category='error')
        else:
            # Passed all checks, user will be added to database
            flash('Account created', category='success')
    return render_template("signUp.html")

    