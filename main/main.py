from flask import Blueprint, request, render_template

main_blueprint = Blueprint('main', __name__, template_folder='templates')
@main_blueprint.route('/')
def main():
    return render_template('index.html')
