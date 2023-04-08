from flask import Blueprint

from src.services.shows import ShowService


bp = Blueprint("shows", __name__, url_prefix="/shows")

bp.add_url_rule(
    "",
    view_func=ShowService.as_view("shows")
)