from datetime import datetime
from flask import Blueprint, render_template, request, session
from ..models.project import *


bp = Blueprint('index', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():

    def extract_date(date):
        year = int(date[0:4])
        if date[6] == '-':
            month = int(date[5:6])
            date = int(date[7:])
        else:
            month = int(date[5:7])
            date = int(date[8:])

        result = (year, month, date)
        return result

    if request.method == 'POST':
        start = extract_date(request.form['start_date'])
        end = extract_date(request.form['end_date'])
        start_date = datetime(start[0], start[1], start[2])
        end_date = datetime(end[0], end[1], end[2])
        cid = find_cid(request.form['course_subject'],
                       request.form['course_number'])
        create_project(request.form['assignment_type'], cid, start_date, end_date,
                       request.form['title'], request.form['description'], session.get('aid'))
        # create_project(request.form['assignment_type'], 1, datetime(2022, 1, 1), datetime(2022, 12, 31),
        #                request.form['title'], request.form['description'], 1)

    projects = get_all_projects()
    return render_template('index.html', projects=projects)
