from .models import *
from ..db import *
from sqlalchemy import *


def get_all_projects():
    return Project.query.all()


def create_project(title, group_leader, description,  project_start_date, project_end_date):
    new_project = Project(title, group_leader, description,
                          project_start_date, project_end_date)
    db.session.add(new_project)
    db.session.commit()


# Using raw sql with sqlalchemy connection
def get_all_projects_raw():
    # For using sqlalchemy connection
    engine = create_engine("sqlite:///instance/forum_raw.db")
    connection = engine.connect()
    result = connection.execute('SELECT * FROM Project;')
    # connection.close()
    return result


def create_project_raw(title, group_leader, description,  project_start_date, project_end_date):
    engine = create_engine("sqlite:///instance/forum_raw.db")
    connection = engine.connect()
    query = '''INSERT INTO Project (title, group_leader, description, project_start_date, project_end_date)
                       VALUES ('{}', '{}', '{}', '{}', '{}')'''.format(
        title, group_leader, description,  project_start_date, project_end_date)
    connection.execute(query)
    # connection.close()
    return
