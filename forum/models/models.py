from sqlalchemy import Integer, Date, String, Column
from ..db import db


class Project(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    group_leader = Column(String)
    description = Column(String)
    project_start_date = Column(Date)
    project_end_date = Column(Date)

    def __init__(self, title, group_leader, description,  project_start_date, project_end_date):
        self.title = title
        self.group_leader = group_leader
        self.description = description
        self.project_start_date = project_start_date
        self.project_end_date = project_end_date
