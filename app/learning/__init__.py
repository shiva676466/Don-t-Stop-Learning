from flask import Blueprint

learning = Blueprint('learning', __name__, url_prefix='/learning', template_folder='templates')

from . import routes
