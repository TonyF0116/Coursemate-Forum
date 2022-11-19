from datetime import datetime
from flask import Blueprint, render_template, request, session, flash
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
        if len(cid) != 1:
            flash('Invalid course')
            projects = get_all_projects()
            return render_template('index.html', projects=projects, title=request.form['title'],
                                   course_subject=request.form['course_subject'],
                                   course_number=request.form['course_number'],
                                   assignment_type=request.form['assignment_type'],
                                   start_date=request.form['start_date'],
                                   end_date=request.form['end_date'],
                                   description=request.form['description']
                                   )
        else:
            create_project(request.form['assignment_type'], cid[0][0], start_date, end_date,
                           request.form['title'], request.form['description'], session.get('user_id'))

    projects = get_all_projects()
    # print(projects[0][0].__dict__)
    return render_template('index.html', projects=projects)
