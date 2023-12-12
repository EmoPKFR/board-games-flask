from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/shop")
def shop():
    return render_template("shop_info/shop.html")