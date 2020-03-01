from flask import render_template, redirect, url_for, current_app, Blueprint

contact_bp = Blueprint('contact', __name__)


@contact_bp.route('/')
def contact():
    return render_template('contact.html')

