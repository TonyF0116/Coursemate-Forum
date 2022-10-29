from datetime import datetime
from flask import Blueprint, render_template, request
from ..models.project import *


bp = Blueprint('index', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():

    def extract_date(date):
        result_0 = int(date[0:4])
        if date[6] == '-':
            result_1 = int(date[5:6])
            result_2 = int(date[7:])
        else:
            result_1 = int(date[5:7])
            result_2 = int(date[8:])

        result = (result_0, result_1, result_2)
        print(result)
        return result

    if request.method == 'POST':
        start = extract_date(request.form['start_date'])
        end = extract_date(request.form['end_date'])
        start_date = datetime(start[0], start[1], start[2])
        end_date = datetime(end[0], end[1], end[2])
        create_project(request.form['title'], 'User',
                       request.form['description'], start_date, end_date)

    projects = get_all_projects()
    return render_template('index.html', projects=projects)
