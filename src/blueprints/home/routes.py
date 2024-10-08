""" Blueprint for home page endpoint """

from flask import Blueprint, render_template

home_bp = Blueprint("home", __name__, template_folder="templates")


@home_bp.route("/", methods=["GET"])
def home() -> str:
    """
    Home page
    :return: Home page
    """
    return render_template("index.html", title="Home")
