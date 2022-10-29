from flask import Blueprint, render_template
from ..models.project import *


bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    projects = get_all_projects()
    return render_template('index.html', projects=projects)
