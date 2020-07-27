from flask import Blueprint
paises = Blueprint('paises', __name__)
from .views import *