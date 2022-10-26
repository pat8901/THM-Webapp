from flask import Blueprint, render_template

from website.auth import login,logout,sign_up

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")

@views.route("/login")
def login():
    return render_template("login.html")

@views.route("/logout")
def logout():
    return render_template("logout.html")

@views.route("/sign-up")
def sign_up():
    return render_template("signUp.html")