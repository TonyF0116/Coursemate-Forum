from .models import *


def get_all_projects():
    return Project.query.all()


def create_project(title, group_leader, description,  project_start_date, project_end_date):
    new_project = Project(title, group_leader, description,
                          project_start_date, project_end_date)
    db.session.add(new_project)
    db.session.connect
