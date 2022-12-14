from sqlalchemy import ForeignKey, Integer, Date, String, Column
from ..db import db


class Student(db.Model):
    aid = Column(Integer, primary_key=True)
    displayed_name = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    major = Column(String)
    year = Column(Integer)
    preferred_work_time = Column(Integer)

    def __init__(self, displayed_name):
        self.displayed_name = displayed_name


class Account(db.Model):
    aid = Column(Integer, ForeignKey(Student.aid), primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self, aid, username, password):
        self.aid = aid
        self.username = username
        self.password = password


class Course(db.Model):
    cid = Column(Integer, primary_key=True)
    term = Column(String)
    course_subject = Column(String)
    course_number = Column(Integer)

    def __init__(self, term, course_subject, course_number):
        self.term = term
        self.course_subject = course_subject
        self.course_number = course_number


class Course_taken(db.Model):
    aid = Column(Integer, ForeignKey(Student.aid), primary_key=True)
    cid = Column(Integer, ForeignKey(Course.cid), primary_key=True)
    status = Column(Integer)

    def __init__(self, aid, cid, status):
        self.aid = aid
        self.cid = cid
        self.status = status


class Project(db.Model):
    pid = Column(Integer, primary_key=True)
    assignment_type = Column(Integer)
    cid = Column(Integer, ForeignKey(Course.cid))
    start_date = Column(Date)
    end_date = Column(Date)
    title = Column(String)
    description = Column(String)
    captain_id = Column(Integer, ForeignKey(Student.aid))

    def __init__(self, assignment_type, cid, start_date, end_date, title, description, captain_id):
        self.assignment_type = assignment_type
        self.cid = cid
        self.start_date = start_date
        self.end_date = end_date
        self.title = title
        self.description = description
        self.captain_id = captain_id


class Team(db.Model):
    pid = Column(Integer, ForeignKey(Project.pid), primary_key=True)
    aid = Column(Integer, ForeignKey(Student.aid), primary_key=True)

    def __init__(self, pid, aid):
        self.pid = pid
        self.aid = aid


class Course_group(db.Model):
    cid = Column(Integer, ForeignKey(Course.cid), primary_key=True)
    type = Column(Integer)
    entry = Column(String)

    def __init__(self, cid, type, entry):
        self.cid = cid
        self.type = type
        self.entry = entry


class Connection(db.Model):
    sender = Column(Integer, ForeignKey(Student.aid), primary_key=True)
    receiver = Column(Integer, ForeignKey(Student.aid), primary_key=True)
    status = Column(Integer)
    message = Column(String)

    def __init__(self, sender, receiver, status, message):
        self.sender = sender
        self.receiver = receiver
        self.status = status
        self.message = message


class Favourite(db.Model):
    aid = Column(Integer, ForeignKey(Student.aid), primary_key=True)
    pid = Column(Integer, ForeignKey(Project.pid), primary_key=True)

    def __init__(self, aid, pid):
        self.aid = aid
        self.pid = pid
