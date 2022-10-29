from flask import Blueprint, render_template

from website.auth import login,logout,sign_up

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")