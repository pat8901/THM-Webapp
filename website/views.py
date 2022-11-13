from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user
from website.auth import login,logout,sign_up

views = Blueprint('views', __name__)


@views.route('/')
@login_required # User can not get to the homepage unless they are logged in
def home():
    return render_template("home.html")