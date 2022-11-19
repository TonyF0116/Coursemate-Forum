from . import models
from ..db import db


def create_user(username, password):
    new_student = models.Student(username)
    db.session.add(new_student)
    db.session.commit()

    new_account = models.Account(new_student.aid, username, password)
    db.session.add(new_account)
    db.session.commit()


def check_password(username, password):
    user_with_correct_username = models.Account.query.filter_by(
        username=username).all()
    if len(user_with_correct_username) != 1:
        return "Username doesn't exist."

    user_with_correct_password = models.Account.query.filter_by(
        username=username, password=password).all()
    if len(user_with_correct_password) != 1:
        return "Password incorrect."

    return user_with_correct_password[0]


def delete_all_account():
    models.Account.query.delete()
    db.session.commit()
    return "All user deleted."


def list_all_account():
    accounts = models.Account.query.all()
    return accounts
