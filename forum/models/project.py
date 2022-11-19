from .models import *
from ..db import *
from sqlalchemy import *


def get_all_projects():
    return db.session.query(Project, Course).join(Course).order_by(Project.pid.desc()).all()


def create_project(assignment_type, cid, start_date, end_date, title, description, captain_id):
    new_project = Project(assignment_type, cid, start_date,
                          end_date, title, description, captain_id)
    db.session.add(new_project)
    db.session.commit()


def find_cid(course_subject, course_number):
    cur_semester = 'FA2022'
    return Course.query.filter_by(term=cur_semester, course_subject=course_subject, course_number=course_number).with_entities(Course.cid).all()
