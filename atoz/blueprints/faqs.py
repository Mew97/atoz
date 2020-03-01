from flask import render_template, redirect, url_for, current_app, Blueprint

faqs_bp = Blueprint('faqs', __name__)


@faqs_bp.route('/')
def faqs():
    return render_template('faqs.html')


